from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from reviews.models import Review
from supplements.models import Supplement, Nutrient, Functional
from supplements.serializers import SupplementListSerializer
import pandas as pd
from django_pandas.io import read_frame
import numpy as np
from scipy.sparse.linalg import svds
from django.http.response import JsonResponse
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_recommend_supplementList(request):
    reviews = Review.objects.filter(user=request.user.id)
    if len(reviews) == 0:
        res = []
        recommends = supplement_by_rank()

        for i, recommend in recommends.iterrows():
            print(recommend['id'])
            if i == 10:
                break
            supplement = get_object_or_404(Supplement, pk=recommend['id'])
            res.append(supplement)
        serializers = SupplementListSerializer(res, many=True)
        return Response(serializers.data)
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
        if i == 10:
            break
        supplement = get_object_or_404(Supplement, pk=prediction['id'])
        cf_predictions.append(supplement)

    serializers = SupplementListSerializer(cf_predictions, many=True)

    return Response(serializers.data)


# 리뷰 수가 적으면 추천이 제대로 안됨
def collaboration_filtering(df_svd_preds, user_id, ori_supplements_df, ori_ranks_df, num_recommendations=10):
    # print(df_svd_preds)
    # print(user_id)
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_recommend_functional(request):
    data = {}
    # print(request.user.interests)
    for interest in request.user.interests.values():
        print(interest)
        res = []
        recommends = supplement_by_functional(interest['id'])
        if recommends.empty:
            data[interest['name']] = []
            continue

        for i, recommend in recommends.iterrows():
            # print(recommend[1]['id'])
            if i == 10:
                break
            supplement = get_object_or_404(Supplement, pk=recommend['id'])
            res.append(supplement)
        data[interest['name']] = SupplementListSerializer(res, many=True).data
    print(data)
    return Response(data)


def supplement_by_rank():
    df_supplements = read_frame(Supplement.objects.all(), verbose=False)
    df_reviews = read_frame(Review.objects.all(), verbose=False)
    df_reviews.drop(['id', 'title', 'content', 'created_at',
                     'updated_at'], axis=1, inplace=True)

    df_supplements_reviews = df_supplements.merge(
        df_reviews, left_on='id', right_on='supplement')
    ranks_group = df_supplements_reviews.groupby(['id'])
    # print(ranks_group.sum())
    ranks = ranks_group.agg({
        'rank': 'mean',
        'supplement': 'count'
    }).rename(columns={'supplement': 'count'})

    # isEnoughReviews = ranks['count'] >= min_reviews
    # ranks = ranks[isEnoughReviews]

    ranks = ranks.sort_values(by=['rank'], ascending=False)

    return ranks.head(10).reset_index()


def supplement_by_functional(category_id, min_reviews=10):
    functionals = Functional.objects.filter(category=category_id)
    nutrients = []
    for functional in functionals:
        nutrients.extend(
            list(Nutrient.objects.filter(functionals=functional.id)))
    supplements = []
    for nutrient in nutrients:
        supplements.extend(
            Supplement.objects.filter(nutrients=nutrient.id).values()
        )
    df_supplements_category = pd.DataFrame(supplements).drop_duplicates()

    df_reviews = read_frame(Review.objects.all(), verbose=False)
    df_reviews.drop(['id', 'title', 'content', 'created_at',
                     'updated_at'], axis=1, inplace=True)
    # print(df_supplements_category)
    # print(df_reviews)

    df_supplements_reviews = df_supplements_category.merge(
        df_reviews, left_on='id', right_on='supplement')
    # print(df_supplements_reviews)
    ranks_group = df_supplements_reviews.groupby(['id'])
    # print(ranks_group.sum())
    ranks = ranks_group.agg({
        'rank': 'mean',
        'supplement': 'count'
    }).rename(columns={'supplement': 'count'})

    # isEnoughReviews = ranks['count'] >= min_reviews
    # ranks = ranks[isEnoughReviews]

    ranks = ranks.sort_values(by=['rank'], ascending=False)

    return ranks.head(10).reset_index()
