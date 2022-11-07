from django.forms import ModelForm, TextInput, Textarea
from .models import *


class CreatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва статті',
            }),
        }


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Назва статті',
            }),
            'text': Textarea(attrs={
                'placeholder': 'Текст статті',
            }),
        }


class PostImageForm(ModelForm):

    class Meta:
        model = PostImage
        fields = ('image',)


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'placeholder': 'Текст комента',
            }),
        }
