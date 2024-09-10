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

JSON_WITH_INCORRECT_TEXT_FIELD = {
    "text": 123,
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
    get_all_meme_endpoint.check_that_status_is_200()


def test_create_meme(post_meme_endpoint, set_headers, delete_meme_endpoint):
    id_meme = post_meme_endpoint.new_meme(body=TEST_DATA, headers=set_headers)
    post_meme_endpoint.check_that_status_is_200()
    post_meme_endpoint.check_that_url_in_new_meme_is_correct(id_meme=id_meme, headers=set_headers, body=TEST_DATA)
    post_meme_endpoint.check_that_text_in_new_meme_is_correct(id_meme=id_meme, headers=set_headers, body=TEST_DATA)
    delete_meme_endpoint.delete_meme(id_meme=id_meme, headers=set_headers)


def test_get_meme_by_id(get_meme_by_id_endpoint, set_headers):
    get_meme_by_id_endpoint.get_meme_by_id(headers=set_headers)
    get_meme_by_id_endpoint.check_that_status_is_200()


def test_put_meme(put_meme_endpoint, new_id_meme, set_headers):
    id_meme = new_id_meme
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
    put_meme_endpoint.put_meme(
        id_meme=id_meme,
        headers=set_headers,
        body=body)
    put_meme_endpoint.check_that_status_is_200()
    put_meme_endpoint.check_that_id_in_new_meme_is_correct(id_meme=id_meme, headers=set_headers, body=body)
    put_meme_endpoint.check_that_text_in_new_meme_is_correct(id_meme=id_meme, headers=set_headers, body=body)
    put_meme_endpoint.check_that_url_in_new_meme_is_correct(id_meme=id_meme, headers=set_headers, body=body)


def test_delete_meme(delete_meme_endpoint, new_id_meme, set_headers):
    id_meme = new_id_meme
    delete_meme_endpoint.delete_meme(id_meme=id_meme, headers=set_headers)
    delete_meme_endpoint.check_that_status_is_200()
    delete_meme_endpoint.check_that_meme_is_deleted(id_meme=id_meme, headers=set_headers)


def test_create_meme_miss_text_field(post_meme_endpoint, set_headers):
    post_meme_endpoint.new_meme_with_invalid_data(body=WRONG_DATA, headers=set_headers)
    post_meme_endpoint.check_that_status_code_is_400()


def test_create_meme_with_incorrect_data_type(post_meme_endpoint, set_headers):
    post_meme_endpoint.new_meme_with_invalid_data(body=JSON_WITH_INCORRECT_TEXT_FIELD, headers=set_headers)
    post_meme_endpoint.check_that_status_code_is_400()


def test_create_meme_with_wrong_headers(post_meme_endpoint):
    post_meme_endpoint.new_meme_with_invalid_data(body=TEST_DATA, headers=WRONG_HEADERS)
    post_meme_endpoint.check_that_status_is_401()


def test_put_meme_with_wrong_headers(put_meme_endpoint, new_id_meme, headers=WRONG_HEADERS):
    id_meme = new_id_meme
    put_meme_endpoint.put_meme(
        id_meme=id_meme,
        headers=headers,
        body={
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
        )
    put_meme_endpoint.check_that_status_is_401()


def test_put_meme_with_wrong_body(put_meme_endpoint, new_id_meme, set_headers):
    id_meme = new_id_meme
    put_meme_endpoint.put_meme(
        id_meme=id_meme,
        headers=set_headers,
        body={
            "id": id_meme,
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
        )
    put_meme_endpoint.check_that_status_code_is_400()


def test_get_all_meme_with_wrong_headers(get_all_meme_endpoint):
    get_all_meme_endpoint.get_all_meme_with_wrong_token(wrong_headers=WRONG_HEADERS)
    get_all_meme_endpoint.check_that_status_is_401()


def test_get_meme_if_id_is_list(get_meme_by_id_endpoint, set_headers):
    get_meme_by_id_endpoint.get_meme_id_is_list(id_meme=id_list, headers=set_headers)
    get_meme_by_id_endpoint.check_that_status_code_is_404()


def test_delete_meme_with_alien_token(delete_meme_endpoint, new_id_meme):
    id_meme = new_id_meme
    delete_meme_endpoint.delete_meme_with_alien_token(id_meme=id_meme, headers=WRONG_HEADERS)
    delete_meme_endpoint.check_that_status_is_401()
