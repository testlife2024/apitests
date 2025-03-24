import pytest
import requests


def test_createpost():
    data_1 = {
        "title": "title4",
        "body": "description4",
        " userId": 4
    }
    response_1 = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json = data_1
    ).json()
    assert response_1["title"] == data_1["title"]


def test_updatepost():
    data_2 = {
        "title": "title4_2.0",
        "body": "description4",
        " userId": 4
    }
    response_2 = requests.put(
        'https://jsonplaceholder.typicode.com/posts/2',
        json = data_2
    ).json()
    assert response_2["title"] == data_2["title"]


def test_deletepost():
    response_3 = requests.delete('https://jsonplaceholder.typicode.com/posts/4')
    assert response_3.status_code == 200


