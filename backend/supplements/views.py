from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import FunctionalSerializer, NutrientSerializer, SupplementSerializer, NutrientSimpleSerializer, SupplementListSerializer
from .models import Functional, Nutrient, Supplement


@api_view(['GET'])
def getSupplementsList(request, page):
    start, end = (page-1)*8, page*8
    supplements = Supplement.objects.all()[start:end]
    serializers = SupplementListSerializer(supplements, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getSupplementDetail(request, supplement_pk):
    supplement = get_object_or_404(Supplement, pk=supplement_pk)
    serializer = SupplementSerializer(supplement)
    return Response(serializer.data)
