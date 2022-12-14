import os
from config import PATH, SLASH


def setup():
    manage = f'{PATH}{SLASH}manage.py'

    os.system(f'python {manage} makemigrations')
    os.system(f'python {manage} migrate')
