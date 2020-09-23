from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ReviewView.as_view()),
]