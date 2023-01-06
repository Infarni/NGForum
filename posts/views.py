from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .forms import *


class Posts():
    def __init__(self, post, comments, images):
        self.post = post
        self.comments = comments
        self.images = images


def home(request):
    un_formated_posts = Post.objects.order_by('-date')[:100]
    posts = []

    for el in un_formated_posts:
        try:
            comments = Comment.objects.filter(post=el)
        except Comment.DoesNotExist:
            comments = None
        try:
            images = PostImage.objects.filter(post=el)
        except PostImage.DoesNotExist:
            images = None

        posts.append(Posts(el, comments, images))

    data = {
        'posts': posts
    }

    return render(request, 'posts/home.html', data)


def create_post(request):
    if request.user.is_authenticated:
        data = {}
        if request.method == 'POST':
            form = CreatePostForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                form = PostForm(instance=Post.objects.get(pk=instance.pk))
                return redirect('continue_post', instance.pk)
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])
        else:
            form = CreatePostForm()
            data['form'] = form
            print(data)
            return render(request, 'posts/create.html', data)
    return redirect('home')


def continue_post(request, pk):
    data = {}
    post = Post.objects.get(pk=pk)
    if request.user != post.author:
        return redirect('home')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            data['form'] = instance
            return redirect('home')

    form = PostForm(instance=Post.objects.get(pk=pk))
    data['form'] = form
    data['post'] = post
    data['pk_post'] = pk
    return render(request, 'posts/continue_post.html', data)


def post_image(request, pk):
    data = {}
    post = Post.objects.get(pk=pk)
    if request.user != post.author:
        return redirect('home')
    if request.method == 'POST':
        form = PostImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.save()
            images = PostImage.objects.filter(post=post)
            data['form'] = PostImageForm()
            data['images'] = images
            data['pk_post'] = pk
            return render(request, 'posts/post_image.html', data)

    form = PostImageForm()
    images = PostImage.objects.filter(post=post)
    data['form'] = form
    data['images'] = images
    data['pk_post'] = pk
    return render(request, 'posts/post_image.html', data)


def comments(request, pk):
    data = {}
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.author = request.user
            instance.save()

        data['form'] = form
        data['comments'] = comments
        return render(request, 'posts/comments.html', data)

    else:
        form = CommentForm()
        data['form'] = form
        data['comments'] = comments
        return render(request, 'posts/comments.html', data)


def post_view(request, pk):
    data = {}
    post = Post.objects.get(pk=pk)
    images = PostImage.objects.filter(post=post)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    data['post'] = post
    data['images'] = images
    data['comments'] = comments
    data['form'] = form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.author = request.user
            instance.save()
            data['post'] = post
            data['images'] = images
            data['comments'] = comments
            return render(request, 'posts/view.html', data)
        else:
            return render(request, 'posts/view.html', data)
    return render(request, 'posts/view.html', data)


class PostAPIView(APIView):
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
