import os
import platform
from handlers import setup, database, wipe, config


while True:
    print('''
1. Запустити сервер\n
2. Налаштувати проект\n
3. Очистити весь кеш, міграції та базу даних\n
4. Наповнити базу даних (можливо займе 5-10 хв)\n
5. Вийти\n\n''')
    response = int(input('Введіть номер команди: '))
        
    if response == 1:
        os.system('python manage.py runserver')
    elif response == 2:
        setup.setup()
    elif response == 3:
        wipe.wipe(config.DIRS_WIPE, config.FILES_WIPE)
    elif response == 4:
        database.filling()
    elif response == 5:
        break
    else:
        print('Ви ввели невірний номер, повторіть спробу')
