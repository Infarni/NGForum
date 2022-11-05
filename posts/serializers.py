from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'date')


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ('post', 'image')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('post', 'author', 'text', 'date')
