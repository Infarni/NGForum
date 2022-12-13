from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.forms import *
from users.models import *
from posts.models import *
from math import ceil


def users_no_filters(request):
    return redirect('api_users', number=1)



class PostsAllAPIView(APIView):
    def get(self, request):
        posts_unformated = PostModel.objects.order_by('-date_update')
        posts = []

        for post in posts_unformated:
            images_unformated = PostImageModel.objects.filter(post=post)
            images = []
            
            for image in images_unformated:
                images.append(
                    {
                        "id": image.id,
                        "image": image.image.url
                    }
                )
            posts.append(
                {
                    "userId": post.author.id,
                    "id": post.id,
                    "title": post.title,
                    "body": post.text,
                    "images": images,
                    "date_create": post.date_create,
                    "date_update": post.date_update
                }
            )

        return Response(posts)


class PostsAPIView(APIView):
    def get(self, request, number):
        number -= 1
        posts_unformated = PostModel.objects.order_by('-date_update')[number * 4:number * 4 + 4]
        posts = []

        for post in posts_unformated:
            images_unformated = PostImageModel.objects.filter(post=post)
            images = []
            
            for image in images_unformated:
                images.append(
                    {
                        "id": image.id,
                        "image": image.image.url
                    }
                )
            posts.append(
                {
                    "userId": post.author.id,
                    "id": post.id,
                    "title": post.title,
                    "body": post.text,
                    "images": images,
                    "date_create": post.date_create,
                    "date_update": post.date_update
                }
            )

        return Response(posts)


class PostsNumberPagesAPIView(APIView):
    def get(self, request):
        pages = ceil(len(PostModel.objects.order_by('-date_update')) / 4)
        return Response(
            {
                "pages": pages
            }
        )


class PostAPIView(APIView):
    def get(self, request, id):
        post_unformated = get_object_or_404(Post, id=id)
        images_unformated = PostImageModel.objects.filter(post=post_unformated)
        images = []
        
        for image in images_unformated:
            images.append(
                {
                    "id": image.id,
                    "image": image.image.url
                }
            )
        
        post = {
            "userId": post_unformated.author.id,
            "id": post_unformated.id,
            "title": post_unformated.title,
            "body": post_unformated.text,
            "images": images,
            "date_create": post.date_create,
            "date_update": post.date_update
        }

        return Response(post)


class CommentAPIView(APIView):
    def get(self, request, id):
        post = get_object_or_404(PostModel, id=id)
        comments_unformated = PostCommentModel.objects.filter(post=post)
        comments = []
        
        for comment in comments_unformated:
            comments.append(
                {
                    "userId": comment.author.id,
                    "id": comment.id,
                    "body": comment.text,
                    "date_create": comment.date_create,
                    "date_update": comment.date_update
                }
            )
            
        return Response(comments)


class UsersAPIView(APIView):
    def get(self, request, number):
        if number == 1:
            end = 4 * number
        else:
            end = 4 * number - 1
        start = end - 4
        users_unformated = CustomUser.objects.all()[start:end]
        users = []

        for user in users_unformated:
            users.append(
                {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'avatar': user.avatar.url
                }
            )

        return Response(users)


class UserAPIView(APIView):
    def get(self, request, id):
        user_unformated = get_object_or_404(CustomUser, id=id)
        user = {
            'id': user_unformated.id,
            'username': user_unformated.username,
            'email': user_unformated.email,
            'avatar': user_unformated.avatar.url
        }

        return Response(user)
