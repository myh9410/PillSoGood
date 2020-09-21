from django.urls import path
from . import views

name = "supplements"

urlpatterns = [
    path('', views.getSupplementsList),
    path('<int:supplement_pk>/', views.getSupplementDetail)
]
