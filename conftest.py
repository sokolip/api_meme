import pytest
import requests
from endpoints.get_all_meme import GetAllMeme
from endpoints.post_meme import PostMeme
from endpoints.get_meme_by_id import GetMemeById
from endpoints.endpoint import Endpoint
from endpoints.put_meme import PutMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture(autouse=True, scope="module")
def set_headers():
    endpoint = Endpoint()
    headers = endpoint.check_authorization_token()
    return headers


@pytest.fixture()
def new_id_meme(set_headers):
    url = 'http://167.172.172.115:52355/meme'
    response = requests.post(
        url=url,
        json={
            "text": "Bug on backend and frontend",
            "url": "https://images.app.goo.gl/39XELXiPgkeZwAty7",
            "tags": ["QA", "backend", 'frontend'],
            "info": {
                "colors":[
                    "white",
                    "black"
                ],
                "objects": [
                    "picture",
                    "text"
                ]
            }
        },
        headers=set_headers)
    assert response.status_code == 200, 'Meme does not created'
    response = response.json()
    new_id_meme = response['id']
    print(f'Created new meme with id = {new_id_meme}')
    yield new_id_meme
    requests.delete(
        url=f'{url}/{new_id_meme}',
        headers=set_headers
    )
    print(f'Meme with id = {new_id_meme} deleted')


# @pytest.fixture()
# def delete_meme_by_id(id_meme, set_headers):
#     def _delete_meme(id_meme):
#         url = 'http://167.172.172.115:52355/meme'
#         delete_response = requests.delete(
#             url=f'{url}/{id_meme}',
#             headers=set_headers
#         )
#         assert delete_response.status_code == 200, f'Meme with id = {id_meme} not deleted'
#         print(f'Meme with id = {id_meme} deleted')
#     return _delete_meme


# @pytest.fixture()
# def get_deleted_meme(new_id_meme, set_headers):
#     def _get_meme(id_meme):
#         url = 'http://167.172.172.115:52355/meme'
#         response = requests.get(
#             url=f'{url}/{id_meme}',
#             headers=set_headers
#         )
#         assert response.status_code == 404, 'Meme did not deleted '
#     return _get_meme


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
def put_meme_endpoint(new_id_meme, set_headers):
    return PutMeme()


@pytest.fixture()
def delete_meme_endpoint(set_headers):
    return DeleteMeme()
