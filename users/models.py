from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path_avatar(instance, filename):
    return f'users/{instance.username}/avatar.jpg'


class CustomUser(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to=user_directory_path_avatar,
        default='users/default_avatar.jpg'
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'avatar']

    def __str__(self):
        return self.email
