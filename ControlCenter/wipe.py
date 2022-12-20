import os
import shutil


def wipe(dirs_wipe, files_wipe):
    dirs = []


    for files in dirs_wipe:
        dirs.append(os.listdir(os.path.normpath(f'{files}')))


    index = 0
    for dir_el in dirs:
        for file in dir_el:
            if file != '__init__.py' and file != '__pycache__':
                os.remove(os.path.normpath(f'{dirs_wipe[index]}/{file}'))
        
        index += 1


    for file in files_wipe:
        if os.path.isfile(os.path.normpath(f'{file}')):
            os.remove(os.path.normpath(f'{file}'))

    for file in os.listdir(os.path.normpath(f'media/users/')):
        if file != 'default_avatar.jpg':
            shutil.rmtree(os.path.normpath(f'media/users/{file}'))
