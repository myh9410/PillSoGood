from django.urls import path
from . import views

name = "supplements"

urlpatterns = [
    path('list/<int:page>/', views.getSupplementsList),
    path('<int:supplement_pk>/', views.getSupplementDetail)
]
