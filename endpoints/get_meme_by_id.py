import requests
from endpoints.endpoint import Endpoint
import random
import allure


class GetMemeById(Endpoint):
    @allure.step('Get mem by id')
    def get_meme_by_id(self):
        token = Endpoint()
        token = token.check_authorization_token()
        headers = {
            "Authorization": f"{token}"
        }
        id_meme = random.choice([4, 13, 19])
        self.response = requests.get(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        assert self.response.status_code == 200, 'Wrong ID meme'
        print(self.response.json())

