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
        photos = json.load(open(file))
        for photo in photos:
            sizes = photo['sizes']
            max_size_url = max(sizes, key=self.get_largest)['url']


    def get_largest(self, data):
      if data['width'] >= data['height']:
        return data['width']
      else:
        return data['height']

    def download_photo(self, url):
        names = self.get_name()
        r = requests.get(url, stream=True)
        with open(filename, 'wb') as file:
            for chunk in r.iter_content():
                file.write(chunk)
         
    def get_name(self, file):
        pic_likes = []
        pic_date = []
        pic_name = []
        names = json.load(open(file))
        for name in names:
            pic_likes.append(name['likes']['count'])
            pic_date.append(name['date'])

        for i in pic_likes:
            for j in pic_likes:
                if i != j and i.startswith(j):
                    pic_name.append(str(pic_likes[i]) +'.jpg')
                    print(i, j)
        #         else:
        #             pic_name.append(str(pic_likes[i]) + str(pic_date[i]) + '.jpg')
        # print(pic_name)




      

    def write_json(self, data):
        with open('photos.json', 'w') as file_object:
            json.dump(data, file_object, indent=2, ensure_ascii=False)