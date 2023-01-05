import os


URL = 'https://habr.com/ru/'
PATH = os.getcwd()
DIRS_WIPE = [
    f'users/__pycache__',
    f'users/migrations',
    f'users/migrations/__pycache__',
    f'posts/__pycache__',
    f'posts/migrations',
    f'posts/migrations/__pycache__',
    f'api/__pycache__',
    f'api/migrations',
    f'api/migrations/__pycache__',
    f'NGForum/__pycache__'
]
FILES_WIPE = [
    'db.sqlite3',
    'data.json'
]