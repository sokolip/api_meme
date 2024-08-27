import pytest

TEST_DATA = {
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
}


def test_get_all_meme(get_all_meme_endpoint, set_headers):
    get_all_meme_endpoint.get_all_meme(headers=set_headers)


def test_create_meme(post_meme_endpoint, set_headers):
    id_meme = post_meme_endpoint.new_meme(body=TEST_DATA, headers=set_headers)
    post_meme_endpoint.delete_meme(id_meme, headers=set_headers)


def test_get_meme_by_id(get_meme_by_id_endpoint, set_headers):
    get_meme_by_id_endpoint.get_meme_by_id(headers=set_headers)


def test_put_meme(put_meme_endpoint, set_headers):
    id_meme = put_meme_endpoint.new_meme(body=TEST_DATA, headers=set_headers)
    put_meme_endpoint.put_meme(id_meme, headers=set_headers)
    put_meme_endpoint.delete_meme(id_meme, headers=set_headers)


def test_delete_meme(delete_meme_endpoint, set_headers):
    id_meme = delete_meme_endpoint.new_meme(body=TEST_DATA, headers=set_headers)
    delete_meme_endpoint.delete_meme(id_meme, headers=set_headers)
