import requests
import json
from pprint import pprint
from VK import VK
from ya_disk import YandexDisk

with open('token_vk.txt', 'r', encoding='utf-8') as file:
    token = file.read().strip()

with open('token_yadisk.txt', 'r', encoding='utf-8') as file:
    token_ya = file.read().strip()

vk_user = VK(token, '5.131')

data_ = vk_user.get_user_photos('552934290', 'profile')
url = vk_user.photos('photos.json')
name = vk_user.get_name('photos.json')
type = vk_user.photos_types('photos.json')
vk_user.download_photo(url, name, 'Photo')
vk_user.discription_file(name, type)

y = YandexDisk(token_ya)
y.upload_file_to_disk('/Photo/', name)