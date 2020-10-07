from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Review
from supplements.models import Supplement
from .serializers import ReviewSerializer, ReviewListSerializer


@api_view(['GET'])
def get_reviews(request):
    reviews = Review.objects.order_by('-created_at')[:10]
    serializers = ReviewSerializer(reviews, many=True)
    return Response(serializers.data)


class ReviewView(APIView):
    # CR 에서 받는 pk는 supplement_pk
    # UD 에서 받는 pk는 review_pk
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        reviews = Review.objects.filter(supplement=pk).order_by('-pk')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        supplement = get_object_or_404(Supplement, pk=pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supplement=supplement, user=request.user)
            # data = {
            #     'status' : 201,
            #     'message' : "글이 성공적으로 작성되었습니다."
            # }
            # return JsonResponse(data)
            return Response(status=201)
        return Response(status=400)

    def put(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = ReviewListSerializer(review, data=request.data)
        # print(review.user)
        # request user 랑 리뷰 user 랑 다르면 403 뱉음!
        if request.user == review.user:
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            return Response(status=400)
        return Response(status=403)

    def delete(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        if request.user == review.user:
            review.delete()
            return Response(status=200)
        return Response(status=403)
