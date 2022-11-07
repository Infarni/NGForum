from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsAPIView.as_view(), name='api_posts'),
    path('posts/<int:pk>/', views.PostAPIView.as_view(), name='api_post'),
    path('posts/<int:pk>/images/', views.UploadPostImageAPIView.as_view(), name='api_upload_image'),
    path('posts/<int:pk>/comment/', views.CommentAPIView.as_view(), name='api_comment'),
    path('posts/create/', views.CreatePostAPIView.as_view(), name='api_create_post'),
    path('users/', views.UsersAPIView.as_view(), name='api_users'),
    path('users/<int:pk>/', views.UserAPIView.as_view(), name='api_user'),
]
