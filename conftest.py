import pytest
import requests
from endpoints.get_all_meme import GetAllMeme
from endpoints.post_meme import PostMeme
from endpoints.get_meme_by_id import GetMemeById
from endpoints.endpoint import Endpoint

# url = 'http://167.172.172.115:52355'
#
# @pytest.fixture(autouse=True, scope="session")
# def auth_token():
#     body = {
#         "name":"Ivan"
#     }
#     response = requests.post(
#         url=f'{url}/authorize',
#         json=body
#     )
#     assert response.status_code == 200, 'Check token'
#     response = response.json()
#     token_meme = response["token"]
#     print(token_meme)
#     return token_meme


@pytest.fixture(autouse=True, scope="session")
def set_headers():
    headers = Endpoint()
    headers = Endpoint.create_authorization_token()


# @pytest.fixture()
# def get_all_meme_endpoint(auth_token):
#     return GetAllMeme()
#
#
# @pytest.fixture()
# def post_meme_endpoint():
#     return PostMeme()
#
#
# @pytest.fixture()
# def get_meme_by_id_endpoint():
#     return GetMemeById()


