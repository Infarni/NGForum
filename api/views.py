from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import *
from posts.models import *


class PostsAPIView(APIView):
    def get(self, request):
        posts = []

        for post in Post.objects.order_by('-date')[:10]:
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
                    'title': post.title,
                    'images': images,
                    'text': post.text,
                    'comments': comments,
                }
            )

        return Response({'posts': posts})


class PostAPIView(APIView):
    def get(self, request, pk):
        post_unformated = Post.objects.get(pk=pk)
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
            'title': post_unformated.title,
            'images': images,
            'text': post_unformated.text,
            'comments': comments,
        }

        return Response({'post': post})
