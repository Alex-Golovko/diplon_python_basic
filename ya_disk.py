import requests

class YaDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_path(self, dir_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources/"
        params = {
            'path': dir_name
        }
        response = requests.put(url=url, params=params, headers=self.get_headers())

    def _get_upload_link(self, disk_file_path, filename: str):
        if disk_file_path is not isinstance(disk_file_path, str):
            self.create_path(dir_name=disk_file_path)
            target_path = f'{disk_file_path}/{filename}'
        else:
            target_path = filename
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": target_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename, url):
        
        href = self._get_upload_link(disk_file_path=disk_file_path, filename=filename).get("href", "")
        response = requests.put(href, data=url)