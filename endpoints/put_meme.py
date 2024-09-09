import requests
import allure
from endpoints.endpoint import Endpoint


class PutMeme(Endpoint):

    @allure.step('Put meme')
    def put_meme(self, id_meme, headers, body):
        self.response = requests.put(
            url=f'{self.url}/meme/{id_meme}',
            json=body,
            headers=headers
        )


