import allure
import requests


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None

    @allure.step('Create token')
    def create_authorization_token(self, headers=None):
        body = {
            "name":"Ivan"
        }
        self.response = requests.post(
            url=f'{self.url}/authorize',
            json=body
        )
        assert self.response.status_code == 200, 'Check token'
        response = self.response.json()
        token = response["token"]
        return token

    def check_authorization_token(self):
        body = {
            "name":"Ivan"
        }
        name = body["name"]
        token = Endpoint()
        token = token.create_authorization_token()
        headers = {}
        self.response = requests.get(
            url=f'{self.url}/authorize/{token}'
        )
        if self.response.status_code  == 200 and 'Token is alive' in self.response.text:
            print(f'Token is alive, username is {name}')
            headers["Authorization"] = f"{token}"
            return headers
        else:
            print('Token not found')
