from VK import VK


with open('token_vk.txt', 'r', encoding='utf-8') as file:
    token = file.read().strip()

HELP = """
В данной программе происходит скачивание фотографий с профиля Вконтакте
для начала работы Вам необходимо:
1. Создать в каталоге 2 файла в формале txt;
1.1 Файл txt с токеном VK
1.2 Файл txt с токеном Яндекс Диск
2. На Яндекс Диске создать папку 'Photos/'
3. Ввести id пользователя
4. Нажать 'Enter', Вы увидите строку загрузки файлов
5. После загрузки в каталоге появиться файл 'List_photos' с названием и размером фотографии

Список доступных команд:
help - справка по программе

id -  ввести id профиля

exit - команда выхода из программы"""

# vk_user = VK(token, '552934290')
def main():
    print('Программа скачивания фотографий из VK.com на Yandex.disk\n'
          'справка по программе: help\n')
    stop = False
    while not stop:
        command = input("Введите команду:\n")
        if command == "help":
            print(HELP)
        elif command == "id":
            user_id_input = input('Введите id пользователя:№\n')
            user_count_photos = input('Введите количество фотографий на скачивание:\n')
            down_vk = VK(token=token, user_id=user_id_input, count=int(user_count_photos))
            down_vk.upload_photos_ya()
        elif command == "exit":
            print("Спасибо за использование программы")
            stop = True
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()