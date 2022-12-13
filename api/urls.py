from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsAllAPIView.as_view(), name='api_posts_all'),
    path(
        'posts&filter(number=<int:number>)/',
        views.PostsAPIView.as_view(),
        name='api_posts'
    ),
    path(
        'posts&filter(pages)/',
        views.PostsNumberPagesAPIView.as_view(),
        name='api_posts_number_pages'
    ),
    path('posts/<int:id>/', views.PostAPIView.as_view(), name='api_post'),
    path(
        'posts/<int:id>/comment/',
        views.CommentAPIView.as_view(),
        name='api_comment'
    ),
    path('users/', views.users_no_filters, name='api_posts_no_filters'),
    path('users&filter(number=<int:number>)/', views.UsersAPIView.as_view(), name='api_users'),
    path('users/<int:id>/', views.UserAPIView.as_view(), name='api_user'),
]
