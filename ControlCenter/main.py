import os
import config


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
            os.system('python ../manage.py runserver')
        elif response == 2:
            os.system('python setup.py')
        elif response == 3:
            os.system('python wipe.py')
        elif response == 4:
            os.system(f'python {config.PATH}/manage.py shell < database.py')
        elif response == 5:
            break
        else:
            print('Ви ввели невірний номер, повторіть спробу')


if __name__ == '__main__':
    main()
