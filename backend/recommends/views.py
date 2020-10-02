from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from reviews.models import Review
from supplements.models import Supplement
from supplements.serializers import SupplementListSerializer
import pandas as pd
from django_pandas.io import read_frame
import numpy as np
from scipy.sparse.linalg import svds
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_recommend_supplementList(request):
    df_reviews = read_frame(Review.objects.all(), verbose=False)

    # 영양제 데이터프레임
    df_supplements = read_frame(Supplement.objects.all(), verbose=False)

    # 유저-영양제 평점 데이터프레임
    df_reviews = df_reviews[['rank', 'supplement', 'user']]
    df_user_supplement_ranks = df_reviews.pivot_table(
        index='user',
        columns='supplement',
        values='rank'
    ).fillna(0)

    matrix = df_user_supplement_ranks.to_numpy()

    user_ranks_mean = np.mean(matrix, axis=1)

    # 평점 조정
    matrix_user_mean = matrix - user_ranks_mean.reshape(-1, 1)

    # SVD U,sigma Vt 행렬을 구한다.
    U, sigma, Vt = svds(matrix_user_mean, k=2)  # 추후 k 값 수정 필요

    sigma = np.diag(sigma)
    svd_user_predicted_ranks = np.dot(
        np.dot(U, sigma), Vt) + user_ranks_mean.reshape(-1, 1)

    df_svd_preds = pd.DataFrame(
        svd_user_predicted_ranks,
        index=df_user_supplement_ranks.index,
        columns=df_user_supplement_ranks.columns
    )

    # 이미 리뷰 작성한 영양제, 협업 필터링 추천 영양제
    already_rated, predictions = collaboration_filtering(
        df_svd_preds, request.user.id, df_supplements, df_reviews, 10)

    cf_predictions = []
    for i, prediction in predictions.iterrows():
        supplement = get_object_or_404(Supplement, pk=prediction['id'])
        cf_predictions.append(supplement)

    serializers = SupplementListSerializer(cf_predictions, many=True)

    return Response(serializers.data)


# 리뷰 수가 적으면 추천이 제대로 안됨
def collaboration_filtering(df_svd_preds, user_id, ori_supplements_df, ori_ranks_df, num_recommendations=10):
    user_row_number = user_id
    sorted_user_predictions = df_svd_preds.loc[user_row_number].sort_values(
        ascending=False)
    user_data = ori_ranks_df[ori_ranks_df.user == user_id]

    # 위에서 뽑은 user_data와 원본 영화 데이터를 합친다.
    user_history = user_data.merge(
        ori_supplements_df, left_on='supplement', right_on='id')

    # 원본 영화 데이터에서 사용자가 본 영화 데이터를 제외한 데이터를 추출
    recommendations = ori_supplements_df[~ori_supplements_df['id'].isin(
        user_history['supplement'])]

    # 사용자의 영화 평점이 높은 순으로 정렬된 데이터와 위 recommendations를 합친다.
    recommendations = recommendations.merge(pd.DataFrame(
        sorted_user_predictions).reset_index(), left_on='id', right_on='supplement')

    # 컬럼이름 바꾸고 정렬
    recommendations = recommendations.rename(
        columns={user_row_number: 'Predictions'}).sort_values('Predictions')

    return user_history, recommendations
