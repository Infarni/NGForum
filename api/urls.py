from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsAPIView.as_view(), name='api_posts'),
    path('posts/<int:pk>/', views.PostAPIView.as_view(), name='api_post'),
]
