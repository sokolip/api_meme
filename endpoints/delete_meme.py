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
        assert self.response.status_code == 200, 'Meme do not deleted'
        print(f'Meme with id = {id_meme} deleted')

    @allure.step('Delete meme with alien token')
    def delete_meme_with_alien_token(self, id_meme, headers):
        self.response = requests.delete(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        print(self.response.status_code)
        assert self.response.status_code == 401, 'Check token'
