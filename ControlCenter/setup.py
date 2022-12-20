import os
from config import PATH


def setup():
    manage = os.path.normpath(f'{PATH}/manage.py')

    os.system(f'python {manage} makemigrations')
    os.system(f'python {manage} migrate')
