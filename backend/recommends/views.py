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
def get_recommend_supplementList(request):
    # review = get_object_or_404(Review, pk=1)
    # print(review.user.id)
    df_reviews = read_frame(Review.objects.all(), verbose=False)
    df_supplements = read_frame(Supplement.objects.all(), verbose=False)
    # print(df_supplements)
    df_reviews = df_reviews[['rank', 'supplement', 'user']]
    # print(df_reviews)
    df_user_supplement_ranks = df_reviews.pivot_table(
        index='user',
        columns='supplement',
        values='rank'
    ).fillna(0)
    # print(df_user_supplement_ranks)
    matrix = df_user_supplement_ranks.to_numpy()

    user_ranks_mean = np.mean(matrix, axis=1)

    matrix_user_mean = matrix - user_ranks_mean.reshape(-1, 1)
    # print(pd.DataFrame(matrix_user_mean, columns=df_user_supplement_ranks.columns))
    U, sigma, Vt = svds(matrix_user_mean, k=1)
    # print(U.shape)
    # print(sigma.shape)
    # print(Vt.shape)
    sigma = np.diag(sigma)
    svd_user_predicted_ranks = np.dot(
        np.dot(U, sigma), Vt) + user_ranks_mean.reshape(-1, 1)

    df_svd_preds = pd.DataFrame(
        svd_user_predicted_ranks,
        index=df_user_supplement_ranks.index,
        columns=df_user_supplement_ranks.columns
    )
    # print(df_svd_preds)
    # print(df_svd_preds.loc[15, :])
    # print(df_svd_preds.iloc[1])
    # print(df_svd_preds.index)
    # print(request.user)
    already_rated, predictions = collaboration_filtering(
        df_svd_preds, 15, df_supplements, df_reviews, 10)
    # print('----')
    print(predictions)
    cf_predictions = []
    for i, prediction in predictions.iterrows():
        # print(prediction)
        supplement = get_object_or_404(Supplement, pk=prediction['id'])
        cf_predictions.append(supplement)

    serializers = SupplementListSerializer(cf_predictions, many=True)

    return Response(serializers.data)


# 리뷰 수가 적으면 추천이 제대로 안됨
def collaboration_filtering(df_svd_preds, user_id, ori_supplements_df, ori_ranks_df, num_recommendations=10):
    # print(ori_supplements_df)
    # print(ori_ranks_df)
    # print(df_svd_preds)
    user_row_number = user_id
    sorted_user_predictions = df_svd_preds.loc[user_row_number].sort_values(
        ascending=False)
    # print(sorted_user_predictions)
    user_data = ori_ranks_df[ori_ranks_df.user == user_id]
    # print(user_data)

    # 위에서 뽑은 user_data와 원본 영화 데이터를 합친다.
    # print(ori_supplements_df.columns)
    # print(user_data.columns)
    user_history = user_data.merge(
        ori_supplements_df, left_on='supplement', right_on='id')
    # print(user_history)

    # 원본 영화 데이터에서 사용자가 본 영화 데이터를 제외한 데이터를 추출
    recommendations = ori_supplements_df[~ori_supplements_df['id'].isin(
        user_history['supplement'])]
    # print(recommendations.head())
    # print('-------------------')
    # print(sorted_user_predictions)
    # 사용자의 영화 평점이 높은 순으로 정렬된 데이터와 위 recommendations를 합친다.
    recommendations = recommendations.merge(pd.DataFrame(
        sorted_user_predictions).reset_index(), left_on='id', right_on='supplement')
    # print(recommendations.columns)

    # 컬럼이름 바꾸고 정렬
    recommendations = recommendations.rename(
        columns={user_row_number: 'Predictions'}).sort_values('Predictions')
    # print(recommendations)

    return user_history, recommendations
