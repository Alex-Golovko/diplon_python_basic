import requests
import json
from pprint import pprint
from VK import VK

with open('token_vk.txt', 'r', encoding='utf-8') as file:
    token = file.read().strip()

vk_user = VK(token, '5.131')
pprint(vk_user.get_user_photos('552934290', 'profile'))