from django.urls import path
from . import views

name = 'recommends'

urlpatterns = [
    path('', views.get_recommend_supplementList),
    path('functional/', views.get_recommend_functional)
]
