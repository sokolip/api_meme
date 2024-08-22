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


def test_get_all_meme(get_all_meme_endpoint):
    get_all_meme_endpoint.get_all_meme()


def test_create_meme(post_meme_endpoint):
    id_meme = post_meme_endpoint.new_meme(body=TEST_DATA)
    post_meme_endpoint.delete_meme(id_meme)

#
# def test_get_meme_by_id(get_meme_by_id_endpoint):
#     get_meme_by_id_endpoint.get_meme_by_id()


