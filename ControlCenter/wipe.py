import os
import shutil
from config import PATH, SLASH


def wipe(dirs_wipe, files_wipe):
    dirs = []


    for files in dirs_wipe:
        dirs.append(os.listdir(f'{PATH}{SLASH}{files}'))


    index = 0
    for dir_el in dirs:
        for file in dir_el:
            if file != '__init__.py' and file != '__pycache__':
                os.remove(f'{PATH}{SLASH}{dirs_wipe[index]}{SLASH}{file}')
        
        index += 1


    for file in files_wipe:
        if os.path.isfile(f'{PATH}{SLASH}{file}'):
            os.remove(f'{PATH}{SLASH}{file}')

    for file in os.listdir(f'{PATH}{SLASH}media{SLASH}users{SLASH}'):
        if file != 'default_avatar.jpg':
            shutil.rmtree(f'{PATH}{SLASH}media{SLASH}users{SLASH}{file}')
