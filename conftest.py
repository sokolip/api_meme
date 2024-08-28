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