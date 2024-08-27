import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('Create new meme')
    def new_meme(self, body, headers):
        self.response = requests.post(
            url=f'{self.url}/meme',
            json=body,
            headers=headers
        )
        assert self.response.status_code == 200, 'Meme does not created'
        response = self.response.json()
        id_meme = response['id']
        print(f'Created new meme with id = {id_meme}')
        return id_meme

    @allure.step('Delete meme')
    def delete_meme(self, id_meme, headers):
        self.response = requests.delete(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        assert self.response.status_code == 200, 'Meme do not deleted'
        print(f'Meme with id = {id_meme} deleted')
