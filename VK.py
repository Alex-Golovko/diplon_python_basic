from ya_disk import YaDisk
import requests
import json
from tqdm import tqdm

with open('token_yadisk.txt', 'r', encoding='utf-8') as file:
    token_ya = file.read().strip()
    

class VK:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, user_id, count=5, offset=0):
        self.user_id = user_id
        self.count = count
        self.offset = offset
        self.params = {
            'access_token': token,
            'v': '5.131'
        }


    def get_user_photos(self):
        get_photo_url = self.url + 'photos.get'
        get_photo_params = {
            'owner_id': self.user_id,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1,
            'count': self.count,
            'offset': self.offset
        }
        r = requests.get(get_photo_url, params={**self.params, **get_photo_params}).json()
        return r



    def count_photos(self):
        data = self.get_user_photos()
        count_photo = data['response']['count']
        return count_photo


    def get_name_list(self):
        pic_likes = []
        pic_date = []
        base = self.get_user_photos()
        for name in base['response']['items']:
            pic_likes.append(str(name['likes']['count']))
            pic_date.append(str(name['date']))
        idx = [i for i, x in enumerate(pic_likes) if x in filter(lambda x: pic_likes.count(x) > 1, set(pic_likes))]
        for i in idx:
            old_index = pic_likes.pop(i)
            new_index = old_index + '_' + pic_date[i]
            pic_likes.insert(i, new_index)
        return pic_likes
        
    def get_photo_size(self):
        size_type = []
        base = self.get_user_photos()
        for photo in base['response']['items']:
            size_type.append(photo['sizes'][-1]['type'])
        return size_type

    def get_url(self):
        file_url = []
        base = self.get_user_photos()
        for files in base['response']['items']:
            file_url.append(files['sizes'][-1]['url'])
        return file_url


    def download_photo(self):
        photo_list = []
        name_photo = self.get_name_list()
        size = self.get_photo_size()
        all = dict(zip(name_photo, size))
        file_name = []
        for key, value in all.items():
            file_name.append(key + '{}'.format('.jpg'))
            file_name_2 = key + '{}'.format('.jpg')
            photo_dict = {'File name': file_name_2, 'sizes': value}
            photo_list.append(photo_dict)
            with open('List_photos.json', 'w') as file:
                json.dump(photo_list, file)
        return file_name

    def upload_photos_ya(self):
        key_name = self.download_photo()
        url = self.get_url()
        all = dict(zip(key_name, url))
        for key, value in tqdm(all.items(), ascii=True, desc='Загрузка файлов на Яндекс Диск'):
            get_url = requests.get(value)
            upload_ya = YaDisk(token=token_ya)
            upload_ya.upload_file_to_disk('Photos/{}'.format(key), get_url.content)
        