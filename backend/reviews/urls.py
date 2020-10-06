from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_reviews),
    path('<int:pk>/', views.ReviewView.as_view()),
]
