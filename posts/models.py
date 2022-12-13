from django.db import models
from django.conf import settings


def user_directory_path_post_images(instance, filename):
    username = instance.post.author.username
    pk = instance.post.pk
    return f'users/{username}/posts/{pk}/images/{filename}'


class PostModel(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        editable=True
    )
    title = models.CharField('Назва', max_length=256)
    text = models.TextField('Текст', blank=True)
    published = models.BooleanField('Опубліковано', default=False)
    deleted = models.BooleanField('Видалено', default=False)
    date_create = models.DateTimeField('Дата публікації', auto_now_add=True)
    date_update = models.DateTimeField('Дата змінення', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публікація'
        verbose_name_plural = 'Публікації'


class PostImageModel(models.Model):
    post = models.ForeignKey(PostModel, editable=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path_post_images)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Зображеня'
        verbose_name_plural = 'Зображеня'


class PostCommentModel(models.Model):
    post = models.ForeignKey(PostModel, editable=True, on_delete=models.CASCADE,)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        editable=True,
    )
    text = models.TextField('Текст', max_length=512)
    date_create = models.DateTimeField('Дата публікації', auto_now_add=True)
    date_update = models.DateTimeField('Дата змінення', auto_now=True)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комментарі'
