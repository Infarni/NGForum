import os
import config


dirs = []


for files in config.DIRS_WIPE:
    dirs.append(os.listdir(f'{config.PATH_NGFORUM}/{files}'))

index = 0
for dir_el in dirs:
    for file in dir_el:
        if file != '__init__.py' and file != '__pycache__':
            os.remove(f'{config.PATH_NGFORUM}/{config.DIRS_WIPE[index]}/{file}')
    
    index += 1


for file in config.FILES_WIPE:
    if os.path.isfile(f'{config.PATH_NGFORUM}/{file}'):
        os.remove(f'{config.PATH_NGFORUM}/{file}')
