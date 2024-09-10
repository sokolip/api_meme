import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step('Delete meme')
    def delete_meme(self, id_meme, headers):
        self.response = requests.delete(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        print(f'Meme with id = {id_meme} deleted')

    @allure.step('Check that meme was deleted')
    def check_that_meme_is_deleted(self, id_meme, headers):
        url = 'http://167.172.172.115:52355/meme'
        response = requests.get(
            url=f'{url}/{id_meme}',
            headers=headers
            )
        assert response.status_code == 404, 'Meme did not deleted'

    @allure.step('Delete meme with alien token')
    def delete_meme_with_alien_token(self, id_meme, headers):
        self.response = requests.delete(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        assert self.response.status_code == 401, 'Check token'
