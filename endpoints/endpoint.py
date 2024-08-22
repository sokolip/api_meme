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
        # print(token)
        return token

    def check_authorization_token(self):
        body = {
            "name":"Ivan"
        }
        name = body["name"]
        token = Endpoint()
        token = token.create_authorization_token()
        headers = {}
        # print(token)
        self.response = requests.get(
            url=f'{self.url}/authorize/{token}'
        )
        response = self.response.text
        if 'Token is alive' in response:
            print(f'Token is alive, username is {name}')
            headers = {
                "Authorization": f"{token}"
            }
        else:
            print('Token not found')
        return headers


current_token = Endpoint()
current_token.create_authorization_token()
current_token = current_token.check_authorization_token()
print(current_token)

    # @allure.step('Check that response is 200')
    # def check_than_status_is_200(self):
    #     assert self.response.status_code == 200