from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserInterestSerializer,TokenSerializer,UserSerializer



class InterestView(APIView):
    def post(self, request):
        username = request.user
        user = get_object_or_404(CustomUser, username=username)
        serializer = UserInterestSerializer(user, data=request.data)
        if serializer.is_valid():
            if len(request.data['interests']) > 3:
                data = {
                    'status':400,
                    "messages":"관심 증상은 최대 3개까지만 선택가능합니다. :)"
                }
                # return JsonResponse(data)
                return Response(status=400,data=data)
            else:
                serializer.save()
                return Response(status=201)
                # return Response(serializer.data)
        return Response(status=400)
        # return Response(serializer.data)

class DbcheckView(APIView):
    def post(self, request):
        useremail = request.data['email']
        nickname= request.data['nickname']
        print("useremail : ", useremail)
        print("nickname : ",nickname)
        try:
            user = str(CustomUser.objects.get(email=useremail))
        except Exception:
            user= ""
        print(user)
        if nickname==user:
            data={
                "state":'login'
            }
            return Response(status=200,data=data)
        else:
            data={
                "state":'signup'
            }
            return Response(status=200,data=data)
