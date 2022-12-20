import os
import platform
from ControlCenter.setup import setup
from ControlCenter.wipe import wipe
from ControlCenter.parser import parsing
from ControlCenter.database import filling
from ControlCenter.config import DIRS_WIPE, FILES_WIPE, URL


while True:
    print('''
1. Запустити сервер\n
2. Налаштувати проект\n
3. Очистити весь кеш, міграції та базу даних\n
4. Спарсити пости та користувачів (Можливо займе 10-20 хв)\n
5. Наповнити базу даних (можливо займе 5-10 хв)\n
6. Встановити всі пакети-залежності\n
7. Вийти\n\n''')
    response = int(input('Введіть номер команди: '))
        
    if response == 1:
        os.system(os.path.normpath(f'python manage.py runserver'))
    elif response == 2:
        setup()
    elif response == 3:
        wipe(DIRS_WIPE, FILES_WIPE)
    elif response == 4:
        parsing(URL)
    elif response == 5:
        filling()
    elif response == 6:
        os_name = platform.system()
        if os_name == 'Windows':
            os.system(os.path.normpath('ControlCenter/package_install.bat'))
        elif os_name == 'Linux':
            os.system(os.path.normpath('sh ControlCenter/package_install.sh'))
        else:
            print('Unknow os')
            break
    elif response == 7:
        break
    else:
        print('Ви ввели невірний номер, повторіть спробу')
