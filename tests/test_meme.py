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


#negative data
WRONG_DATA = {
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

WRONG_HEADERS = {"Authorization": "D123450WtEZM6we"}
id_list = [1, 2]


def test_get_all_meme(get_all_meme_endpoint, set_headers):
    get_all_meme_endpoint.get_all_meme(headers=set_headers)


def test_create_meme(post_meme_endpoint, set_headers, delete_meme_by_id):
    id_meme = post_meme_endpoint.new_meme(body=TEST_DATA, headers=set_headers)
    post_meme_endpoint.check_that_status_is_200()
    delete_meme_by_id(id_meme=id_meme)


def test_get_meme_by_id(get_meme_by_id_endpoint, set_headers):
    get_meme_by_id_endpoint.get_meme_by_id(headers=set_headers)


def test_put_meme(put_meme_endpoint, new_id_meme, set_headers, delete_meme_by_id, get_deleted_meme):
    id_meme = new_id_meme
    put_meme_endpoint.put_meme(id_meme=id_meme, headers=set_headers)


def test_delete_meme(delete_meme_endpoint, new_id_meme, set_headers, get_deleted_meme):
    id_meme = new_id_meme
    delete_meme_endpoint.delete_meme(id_meme=id_meme, headers=set_headers)
    get_deleted_meme(id_meme=id_meme)


def test_create_meme_invalid_data(post_meme_endpoint, set_headers):
    post_meme_endpoint.new_meme_with_invalid_data(body=WRONG_DATA, headers=set_headers)


def test_get_all_meme_with_wrong_headers(get_all_meme_endpoint):
    get_all_meme_endpoint.get_all_meme_with_wrong_token(wrong_headers=WRONG_HEADERS)


def test_get_meme_if_id_is_list(get_meme_by_id_endpoint, set_headers):
    get_meme_by_id_endpoint.get_meme_id_is_list(id_meme=id_list, headers=set_headers)


def test_delete_meme_with_alien_token(delete_meme_endpoint, new_id_meme, delete_meme_by_id, set_headers):
    id_meme = new_id_meme
    alien_headers = set_headers
    delete_meme_endpoint.delete_meme_with_alien_token(id_meme=id_meme, headers=WRONG_HEADERS)
    delete_meme_by_id(id_meme=id_meme)



