import requests
from endpoints.endpoint import Endpoint
import random
import allure


class GetMemeById(Endpoint):
    @allure.step('Get mem by id')
    def get_meme_by_id(self, headers):
        id_meme = random.choice([4, 13, 19])
        self.response = requests.get(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        response = self.response.json()
        assert response['id'] == id_meme

    @allure.step('Get meme when id is list')
    def get_meme_id_is_list(self, id_meme, headers):
        self.response = requests.get(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
