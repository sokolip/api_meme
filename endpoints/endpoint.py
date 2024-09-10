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

    def check_that_url_in_new_meme_is_correct(self, id_meme, headers, body=None):
        self.response = requests.get(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        response = self.response.json()
        assert response['url'] == body['url']

    def check_that_text_in_new_meme_is_correct(self, id_meme, headers, body=None):
        self.response = requests.get(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        response = self.response.json()
        assert response['text'] == body['text']

    def check_that_id_in_new_meme_is_correct(self, id_meme, headers, body=None):
        self.response = requests.get(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        response = self.response.json()
        assert response['id'] == f'{id_meme}'

    def check_that_info_in_new_meme_is_correct(self, id_meme, headers, body=None):
        self.response = requests.get(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        response = self.response.json()
        assert response['info'] == body['info']

    #
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    def check_that_status_is_401(self):
        assert self.response.status_code == 401

    def check_that_status_code_is_400(self):
        assert self.response.status_code == 400

    def check_that_status_code_is_404(self):
        assert self.response.status_code == 404
