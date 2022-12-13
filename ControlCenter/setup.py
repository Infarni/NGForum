import os
import config

manage = f'{config.PATH}/manage.py'

os.system(f'python {manage} makemigrations')
os.system(f'python {manage} migrate')