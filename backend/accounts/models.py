from django.contrib.auth.models import AbstractUser
from django.db import models

# 사용자 지정 필드 추가하기
class CustomUser(AbstractUser):
    birth = models.DateField(null=True)
    gender = models.BooleanField(null=True)
