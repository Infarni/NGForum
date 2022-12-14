import os
from setup import setup
from wipe import wipe
from config import SLASH, PATH, DIRS_WIPE, FILES_WIPE


def main():
    while True:
        print('''
            1. Запустити сервер\n
            2. Налаштувати проект\n
            3. Очистити весь кеш, міграції та базу даних\n
            4. Наповнити базу даних (можливо займе 10-20 хв)\n
            5. Вийти\n\n''')
        response = int(input('Введіть номер команди: '))
        
        if response == 1:
            os.system(f'python ..{SLASH}manage.py runserver')
        elif response == 2:
            setup()
        elif response == 3:
            wipe(DIRS_WIPE, FILES_WIPE)
        elif response == 4:
            os.system(f'python {PATH}{SLASH}manage.py shell < database.py')
        elif response == 5:
            break
        else:
            print('Ви ввели невірний номер, повторіть спробу')


if __name__ == '__main__':
    main()
