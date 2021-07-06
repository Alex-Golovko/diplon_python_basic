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
        self.write_json(r['response']['items'])


    def photos(self, file):
        size_url = []
        photos = json.load(open(file))
        for photo in photos:
            sizes = photo['sizes']
            max_size_url = max(sizes, key=self.get_largest)['url']
            size_url.append(max_size_url)
        print(size_url)
        


    def get_largest(self, data):
      if data['width'] >= data['height']:
        return data['width']
      else:
        return data['height']

    def download_photo(self, filename):
        url = 'https://sun9-28.userapi.com/impf/c850732/v850732336/16fa43/3b7pxN3vzmI.jpg?size=400x400&quality=96&sign=e43d16ae62020287b2e5ae9073d3f878&c_uniq_tag=5rB9bM19KvnvwLaYvsXilF2uT-MWISzsiNrvNJH65UQ&type=album'
        names = self.get_name(filename)[0]
        # for i in range(len(url)):
        r = requests.get(url[i], stream=True)
            # for j in range(len(names)):
            with open(names[j], 'wb') as file:
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
            new_index = old_index + pic_date[i]
            pic_likes.insert(i, new_index)
        return pic_likes
        
    def get_name(self, names):
        name_list = self.get_name_list(names)
        name = []
        for pic_name in name_list:
            name.append(pic_name + '.jpg')
        return name
        
    def write_json(self, data):
        with open('photos.json', 'w') as file_object:
            json.dump(data, file_object, indent=2, ensure_ascii=False)
