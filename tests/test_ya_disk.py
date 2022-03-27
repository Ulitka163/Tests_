import pytest
import requests
from ya_disk import YaCreate

class TestClassPytest:
    def setup(self):
        print('===> setup')

    def teardown(self):
        print('===>teardown')

    def test_YaCreate(self):
        token = ''
        disk_file = '123'
        uploader = YaCreate(token)
        result = uploader.create_file(disk_file)
        assert result[1] == 201

    def test_search_file(self):
        token = ''
        disk_file = '123'
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': disk_file}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        status_code = response.status_code
        assert status_code == 200


