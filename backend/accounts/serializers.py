from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework.authtoken.models import Token



class CustomRegisterSerializer(RegisterSerializer):
    birth = serializers.DateField(required=True)
    gender = serializers.BooleanField(required=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['birth'] = self.validated_data.get('birth', '')
        data_dict['gender'] = self.validated_data.get('gender', '')

        return data_dict

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email','birth','gender']

class TokenSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Token
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','username','is_staff']

class UserInterestSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = CustomUser
        fields = ['interests','user']
        read_only_fields = ['user']