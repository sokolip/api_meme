import pytest
import requests
import allure
from endpoints.endpoint import Endpoint


class PostMeme(Endpoint):
    @allure.step('Create new meme')
    def new_meme(self, body, headers):
        self.response = requests.post(
            url=f'{self.url}/meme',
            json=body,
            headers=headers
        )
        response = self.response.json()
        id_meme = response['id']
        print(f'Created new meme with id = {id_meme}')
        # assert response['text'] == body['text']
        return id_meme

    @allure.step('Invalid data')
    def new_meme_with_invalid_data(self, body, headers):
        self.response = requests.post(
            url=f'{self.url}/meme',
            json=body,
            headers=headers
        )
