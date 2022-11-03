from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/continue_post', views.continue_post, name='continue_post'),
    path('<int:pk>/post_image', views.post_image, name='post_image'),
    path('<int:pk>/comments', views.comments, name='comments')
]
