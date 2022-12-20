import os


def setup():
    os.system(f'python manage.py makemigrations')
    os.system(f'python manage.py migrate')
