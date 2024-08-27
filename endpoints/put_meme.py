import requests
import allure
from endpoints.endpoint import Endpoint


class PutMeme(Endpoint):

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

    @allure.step('Put meme')
    def put_meme(self, id_meme, headers):
        body = {
            "id": id_meme,
            "text": "Zero bug policy",
            "url": "https://memchik.ru/show/5b056ae6b1c7e33a545d79db?page=5",
            "tags": ["QA", "BLM", "Picture"],
            "info": {
                "colors": [
                    "white",
                    "black",
                    "grey"
                ],
                "objects":[
                    "picture",
                    "foto",
                    "text"
                ]
            }
        }
        self.response = requests.put(
            url=f'{self.url}/put/meme/{id_meme}',

            json=body,
            headers=headers
        )
        # print(f'{id_meme_body}, {body}')
        # assert self.response.status_code == 200, 'Wrong status code'

    @allure.step('Delete meme')
    def delete_meme(self, id_meme, headers):
        self.response = requests.delete(
            url=f'{self.url}/meme/{id_meme}',
            headers=headers
        )
        assert self.response.status_code == 200, f'Meme with id = {id_meme} does not deleted'
        print(f'Meme with id = {id_meme} deleted')
