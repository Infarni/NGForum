from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        editable=False,
    )
    title = models.CharField('Назва', max_length=256)
    text = models.TextField('Текст', blank=True)
    date = models.DateTimeField('Дата публікації', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публікація'
        verbose_name_plural = 'Публікації'


def user_directory_path_post_images(instance, filename):
    username = instance.post.author.username
    pk = instance.post.pk
    return f'users/{username}/posts/{pk}/images/{filename}'


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        default=None,
        editable=True,
    )
    image = models.ImageField(upload_to=user_directory_path_post_images)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'Зображеня'
        verbose_name_plural = 'Зображеня'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        default=None,
        editable=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        editable=False,
    )
    text = models.TextField('Текст', max_length=512)
    date = models.DateTimeField('Дата публікації', auto_now_add=True)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комментарі'
