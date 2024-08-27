import pytest
import requests
from endpoints.get_all_meme import GetAllMeme
from endpoints.post_meme import PostMeme
from endpoints.get_meme_by_id import GetMemeById
from endpoints.endpoint import Endpoint
from endpoints.put_meme import PutMeme
from endpoints.delete_meme import DeleteMeme

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


@pytest.fixture(autouse=True, scope="module")
def set_headers():
    endpoint = Endpoint()
    headers = endpoint.check_authorization_token()
    return headers


@pytest.fixture()
def get_all_meme_endpoint(set_headers):
    return GetAllMeme()


@pytest.fixture()
def post_meme_endpoint(set_headers):
    return PostMeme()


@pytest.fixture()
def get_meme_by_id_endpoint(set_headers):
    return GetMemeById()


@pytest.fixture()
def put_meme_endpoint(set_headers):
    return PutMeme()


@pytest.fixture()
def delete_meme_endpoint(set_headers):
    return DeleteMeme()