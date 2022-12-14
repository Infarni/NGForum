import platform

OS = platform.system()
if OS == 'Windows':
    SLASH = '\\'
else:
    SLASH = '/'

URL = 'https://jsonplaceholder.typicode.com/'
PATH = f'..{SLASH}'
DIRS_WIPE = [
    f'users{SLASH}__pycache__',
    f'users{SLASH}migrations',
    f'users{SLASH}migrations{SLASH}__pycache__',
    f'posts{SLASH}__pycache__',
    f'posts{SLASH}migrations',
    f'posts{SLASH}migrations{SLASH}__pycache__',
    f'api{SLASH}__pycache__',
    f'api{SLASH}migrations',
    f'api{SLASH}migrations{SLASH}__pycache__',
    f'NGForum{SLASH}__pycache__'
]
FILES_WIPE = [
    'db.sqlite3'
]