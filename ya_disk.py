import requests
from pprint import pprint

class YaCreate:
    def __init__(self, token: str):
        self.token = token

    def create_file(self, disk_file: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': disk_file}
        response = requests.put(url, headers=headers, params=params)
        response.raise_for_status()
        status_code = response.status_code
        if status_code == 201:
            print('Успешно')
        return response.json(), status_code


if __name__ == '__main__':
    disk_file = 'qwerty'
    token = ''
    uploader = YaCreate(token)
    uploader.create_file(disk_file)