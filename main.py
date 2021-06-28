import  requests
from pprint import pprint
from jsonfile import file_json_process
import json

#Дипломный проект

# Автор: Головко Александр Владимирович
#
# 2021
#
#
# Нужно написать программу, которая будет:
#
# Получать фотографии с профиля. Для этого нужно использовать метод photos.get.
# Сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске.
# Для имени фотографий использовать количество лайков.
# Сохранять информацию по фотографиям в json-файл с результатами.
# Входные данные:
# Пользователь вводит:
#
# id пользователя vk;

class VkProcessing:

    ACCESS_TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

    def __init__(self, user_id):
        self.user_id = user_id

    def get_user_photo(self, user_id):
        params = {
            'access token': self.ACCESS_TOKEN,
            'user_id': user_id,
            'v': '5.77',
            'photo_size': '1',
            'extented': '1',
            'count': '5'
        }
        response = requests.get('https://api.vk.com/method/photos.get', params=params)
        try:
            pprint(response.json())
            return response.json()
        except KeyError:
            return []

