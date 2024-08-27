import requests
import allure
from endpoints.endpoint import Endpoint


class GetAllMeme(Endpoint):
    @allure.step('Get all meme')
    def get_all_meme(self, headers):
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers=headers
        )
        assert self.response.status_code == 200, 'Response status code is not 200'
        response = self.response.json()
