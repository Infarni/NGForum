import os
import shutil
import config


dirs = []


for files in config.DIRS_WIPE:
    dirs.append(os.listdir(f'{config.PATH}/{files}'))


index = 0
for dir_el in dirs:
    for file in dir_el:
        if file != '__init__.py' and file != '__pycache__':
            os.remove(f'{config.PATH}/{config.DIRS_WIPE[index]}/{file}')
    
    index += 1


for file in config.FILES_WIPE:
    if os.path.isfile(f'{config.PATH}/{file}'):
        os.remove(f'{config.PATH}/{file}')

for file in os.listdir(f'{config.PATH}/media/users/'):
    if file != 'default_avatar.jpg':
         shutil.rmtree(f'{config.PATH}/media/users/{file}')
