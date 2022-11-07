from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.forms import *
from users.models import *
from posts.models import *


def posts_no_filters(request):
    return redirect('api_posts', start=0, end=len(Post.objects.all()))


class PostsAPIView(APIView):
    def get(self, request, start, end):
        posts_unformated = Post.objects.order_by('-date')[start:end]
        posts = []

        for post in posts_unformated:
            images_unformated = PostImage.objects.filter(post=post)
            images = []
            comments_unformated = Comment.objects.filter(post=post)
            comments = []

            for img in images_unformated:
                images.append({'image': img.image.url})

            for comment in comments_unformated:
                comments.append(
                    {
                        'author_avatar': comment.author.avatar.url,
                        'author_username': comment.author.username,
                        'author_id': comment.author.id,
                        'text': comment.text,
                        'date': comment.date
                    }
                )

            posts.append(
                {
                    'author_avatar': post.author.avatar.url,
                    'author_username': post.author.username,
                    'id': post.id,
                    'title': post.title,
                    'images': images,
                    'text': post.text,
                    'comments': comments,
                }
            )

        return Response(posts)


class PostAPIView(APIView):
    def get(self, request, pk):
        post_unformated = get_object_or_404(Post, pk=pk)
        images_unformated = PostImage.objects.filter(post=post_unformated)
        images = []
        comments_unformated = Comment.objects.filter(post=post_unformated)
        comments = []

        for img in images_unformated:
            images.append({'image': img.image.url})

        for comment in comments_unformated:
            comments.append(
                {
                    'author_avatar': comment.author.avatar.url,
                    'author_username': comment.author.username,
                    'author_id': comment.author.id,
                    'text': comment.text,
                    'date': comment.date
                }
            )

        post = {
            'author_avatar': post_unformated.author.avatar.url,
            'author_username': post_unformated.author.username,
            'id': post_unformated.id,
            'title': post_unformated.title,
            'images': images,
            'text': post_unformated.text,
            'comments': comments,
        }

        return Response(post)


class CreatePostAPIView(APIView):
    def post(self, request):
        post_object = PostForm(request.POST)

        if post_object.is_valid():
            instance = post_object.save(commit=False)
            instance.author = request.user
            instance.save()

            return Response(
                {
                    'author_avatar': instance.author.avatar.url,
                    'author_username': instance.author.username,
                    'author_id': instance.author.id,
                    'title': instance.title,
                    'text': instance.text,
                    'date': instance.date
                }
            )


class UploadPostImageAPIView(APIView):
    def post(self, request, pk):
        post_object = get_object_or_404(Post, pk=pk)
        image = PostImageForm(request.POST, request.FILES)
        if image.is_valid():
            instance = image.save(commit=False)
            instance.post = post_object
            instance.save()

        images_unformated = PostImage.objects.filter(post=post_object)
        images = []

        for img in images_unformated:
            images.append(
                {'url': img.image.url}
            )
        return Response(
            {
                'post': post_object.id,
                'images': images
            }
        )


class CommentAPIView(APIView):
    def post(self, request, pk):
        post_object = get_object_or_404(Post, pk=pk)
        comments = []
        comment = CommentForm(request.POST)

        if comment.is_valid():
            instance = comment.save(commit=False)
            instance.post = post_object
            instance.author = request.user
            instance.save()

            for comm in Comment.objects.filter(post=post_object):
                comments.append(
                    {
                        'author_id': comm.author.id,
                        'author_avatar': comm.author.avatar.url,
                        'author_username': comm.author.username,
                        'text': comm.text,
                        'date': comm.date
                    }
                )

            return Response(
                {
                    'comments': comments
                }
            )


class UsersAPIView(APIView):
    def get(self, request):
        users_unformated = CustomUser.objects.all()
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

        return Response({'users': users})


class UserAPIView(APIView):
    def get(self, request, pk):
        user_unformated = get_object_or_404(CustomUser, pk=pk)
        user = {
            'user': user_unformated.id,
            'username': user_unformated.username,
            'email': user_unformated.email,
            'avatar': user_unformated.avatar.url
        }

        return Response({'user': user})
