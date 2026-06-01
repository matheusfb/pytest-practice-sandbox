import pytest
import requests
from config import BASE_REST_API_URL

@pytest.mark.rest_api
def test_get_objects_rest_api():
    response = requests.get(BASE_REST_API_URL)
    body = response.json()

    assert response.status_code == 200

    objects = {
        item["name"] for item in body
    }

    assert "Google Pixel 6 Pro" in objects
    assert "Apple iPad Air" in objects

@pytest.mark.rest_api
def test_post_object_rest_api():
    request_body = {
        'name': 'Apple MacBook Pro 15',
        'data': {
            'year': 2019,
            'price': 1849.99,
            'CPU model': 'Intel Core i9',
            'Hard disk size': '1 TB'
        }
    }

    headers  = {
        'Content-Type': 'application/json'
    }

    response = requests.post(
        BASE_REST_API_URL,
        json=request_body,
        headers=headers
    )
    body = response.json()

    assert response.status_code == 200
    assert "Apple MacBook Pro 15" in body["name"]
