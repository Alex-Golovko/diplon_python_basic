import requests
import json


class VK:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_user(self, user_id):
        get_user_url = self.url + 'users.get'
        get_user_params = {
            'user_id': user_id
        }
        r = requests.get(get_user_url, params={**self.params, **get_user_params}).json()
        return r

    def get_user_photos(self, id, album_id):
        get_photo_url = self.url + 'photos.get'
        get_photo_params = {
            'owner_id': id,
            'album_id': album_id,
            'extended': 1,
            'photo_sizes': 1
        }
        r = requests.get(get_photo_url, params={**self.params, **get_photo_params}).json()
        sizes = []
        photos = r['response']['items']
        for i in photos[0:]:
            sizes.append('{}'.format(i['sizes']))
        return sizes

    def max_sizes(self, data):
        

    def write_json(self, data):
        with open('response.json', 'w') as file_object:
            json.dump(data, file_object, indent=2, ensure_ascii=False)