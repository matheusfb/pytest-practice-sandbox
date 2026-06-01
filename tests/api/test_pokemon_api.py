import pytest
import requests

from config import BASE_POKEMON_API_URL

@pytest.mark.pokemon_api
def test_pikachu_pokemon_api():
    response = requests.get(f"{BASE_POKEMON_API_URL}/pokemon/pikachu")
    body = response.json()

    assert response.status_code == 200
    assert "pikachu" in response.text

    types = {
        item["type"]["name"]
        for item in body["types"]
    }
    assert "electric" in types

    moves = {
        move["move"]["name"]
        for move in body["moves"]
    }
    assert "thunderbolt" in moves

@pytest.mark.pokemon_api
def test_pokedex_pokemon_api():
    response = requests.get(f"{BASE_POKEMON_API_URL}/pokemon?limit=151&offset=0")
    body = response.json()

    assert response.status_code == 200

    pokemon_names = {
        pokemon["name"]
        for pokemon in body["results"]
    }

    assert "bulbasaur" in pokemon_names
    assert "mew" in pokemon_names