from rest_framework import serializers
from .models import Review
from accounts.serializers import UserSerializer,UserDetailSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = ['id','title','content','user','rank','created_at','updated_at']
        read_only_fields = ['user','id']

# 리뷰 수정
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','title','content','user','rank']
        read_only_fields = ['user','id']
