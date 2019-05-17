from pprint import pprint
import requests
from urllib.parse import urlencode

APP_ID = 6986722
BASE_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'response_type': 'token',
    'scope': 'status',
    'v': '5.95'
}

# print('?'.join((BASE_URL, urlencode(auth_data))))

TOKEN = ''

params = {
    'access_token': TOKEN,
    'v': '5.95'
}

response = requests.get('https://api.vk.com/method/status.get', params)

print(response.json())

class Friends:
    def __init__(self, token, source_uid, target_uid):
        self.token = token
        self.source_uid = source_uid
        self.target_uid = target_uid

    def get_params(self):
        return dict(
            access_token=self.token,
            v='5.95',
            source_uid=self.source_uid,
            target_uid=self.target_uid,
        )

    def user(self):
        params = self.get_params()
        return f'https://vk.com/id{self.source_uid}'

    def get_mutual_friends(self):
        params = self.get_params()
        response = requests.get(
            f'https://api.vk.com/method/friends.getMutual?params[source_uid]={self.source_uid}&params[target_uid]={self.target_uid}&v=5.95',
            params
        )
        return response.json()
