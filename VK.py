import os
import requests
import json
from pprint import pprint




class VK:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }


    def get_user_photos(self, id, album_id):
        get_photo_url = self.url + 'photos.get'
        get_photo_params = {
            'owner_id': id,
            'album_id': album_id,
            'extended': 1,
            'photo_sizes': 1
        }
        r = requests.get(get_photo_url, params={**self.params, **get_photo_params}).json()
        self.write_json(r['response']['items'], 'photos')


    def photos(self, file):
        size_url = []
        photos = json.load(open(file))
        for photo in photos:
            sizes = photo['sizes']
            max_size_url = max(sizes, key=self.get_largest)['url']
            size_url.append(max_size_url)
        return size_url
        
    def photos_types(self, file):
        size_type = []
        photos_type = json.load(open(file))
        for photo in photos_type:
            types = photo['sizes']
            max_size_type = max(types, key=self.get_largest)['type']
            size_type.append(max_size_type)
        return size_type


    def get_largest(self, data):
      if data['width'] >= data['height']:
        return data['width']
      else:
        return data['height']

    def make_dir(self, dir_name):
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

    def download_photo(self, url, name, dir_name):
        url_photo = url
        name_photo = name
        all = dict(zip(name_photo, url_photo))
        self.make_dir(dir_name)
        for key, value in all.items():
            r = requests.get(value, stream=True)
            with open(f'{dir_name}/{key}', 'wb') as file:
                for chunk in r.iter_content(4096):
                    file.write(chunk)
         
    def get_name_list(self, file):
        pic_likes = []
        pic_date = []
        names = json.load(open(file))
        for name in names:
            pic_likes.append(str(name['likes']['count']))
            pic_date.append(str(name['date']))
        idx = [i for i, x in enumerate(pic_likes) if x in filter(lambda x: pic_likes.count(x) > 1, set(pic_likes))]
        for i in idx:
            old_index = pic_likes.pop(i)
            new_index = old_index + '_' + pic_date[i]
            pic_likes.insert(i, new_index)
        return pic_likes
        
    def get_name(self, name_l):
        name_list = self.get_name_list(name_l)
        name = []
        for pic_name in name_list:
            name.append(pic_name + '.jpg')
        return name

    def discription_file(self, name, type_sizes):
        discript_dict = []
        key_name = name
        sizes = type_sizes
        for i in range(len(key_name)):
            discript_dict.append({"file_name": name[i], "sizes": sizes[i]})
        self.write_json(discript_dict, 'discription')

    def write_json(self, data, name):
        with open(name + '.json', 'w') as file_object:
            json.dump(data, file_object, indent=2, ensure_ascii=False)
