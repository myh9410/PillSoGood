from django.urls import path
from . import views

name = "accounts"

urlpatterns = [
    path('interest/', views.InterestView.as_view()),
    path('check', views.DbcheckView.as_view()),
]
