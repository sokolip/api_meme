import requests
import allure
from endpoints.endpoint import Endpoint


class PutMeme(Endpoint):

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
                "objects": [
                    "picture",
                    "foto",
                    "text"
                ]
            }
        }
        self.response = requests.put(
            url=f'{self.url}/meme/{id_meme}',
            json=body,
            headers=headers
        )
        assert self.response.status_code == 200
        response = self.response.json()
        assert response['text'] == body['text']
