import pytest
import requests

@pytest.mark.api
def test_pokemon_api():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"

    response = requests.get(url)
    body = response.json()

    assert response.status_code == 200

    types = [
        item["type"]["name"]
        for item in body["types"]
    ]

    assert "electric" in types