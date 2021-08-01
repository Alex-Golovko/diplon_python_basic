from VK import VK

HELP = """
В данной программе происходит скачивание фотографий с профиля Вконтакте
для начала работы Вам необходимо:
1. Ввести свой token VK
2. Ввести свой токен Яндекс Диска
3. Ввести id пользователя
4. Нажать 'Enter', Вы увидите строку загрузки файлов
5. После загрузки в каталоге появиться файл 'List_photos' с названием и размером фотографии

Список доступных команд:
help - справка по программе

id -  ввести id профиля

exit - команда выхода из программы"""

print('Программа скачивания фотографий из VK.com на Yandex.disk\n'
      'справка по программе: help\n')
stop = False
while not stop:
    command = input("Введите команду:\n")
    if command == "help":
        print(HELP)
    elif command == "id":
        user_token_vk = input('Введите token VK:\n')
        user_id_input = input('Введите id пользователя:№\n')
        down_vk = VK(token=user_token_vk, user_id=user_id_input)
        print(f'У пользователя {user_id_input} количество фотографий в профиле: {down_vk.count_photos()}\n')
        count_photo = int(input('Введите количество фотографий для скачивания:\n'))
        user_token_ya = input('Введите token YandexDisk:\n')
        down_vk = VK(token=user_token_vk, user_id=user_id_input, count=count_photo)
        down_vk.upload_photos_ya(user_token_ya)
    elif command == "exit":
        print("Спасибо за использование программы")
        stop = True
    else:
        print("Неизвестная команда")
