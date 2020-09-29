from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


from supplements.models import Functional


# 사용자 지정 필드 추가하기
class CustomUser(AbstractUser):
    birth = models.DateField(null=True)
    gender = models.BooleanField(null=True)
    interests = models.ManyToManyField(Functional, related_name='users', blank=True)
