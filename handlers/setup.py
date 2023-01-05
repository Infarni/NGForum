import os


def setup():
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')
