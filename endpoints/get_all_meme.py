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

    @allure.step('Unauthorize requests')
    def get_all_meme_with_wrong_token(self, wrong_headers):
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers=wrong_headers
        )
