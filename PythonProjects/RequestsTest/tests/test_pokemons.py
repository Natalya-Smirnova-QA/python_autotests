import requests
import pytest
import json

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9f68bedd420a3ee5251cf9c7b040bfd6'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN }
TRAINER_ID = '19208'


def test_status_code():
    response = requests.get (url = f'{URL}/pokemons', params= {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get =  requests.get (url = f'{URL}/pokemons', params= {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'

@pytest.mark.parametrize('key, value', [('name','Бульбазавр'), ('trainer_id', TRAINER_ID), ('pokemon_id', '206770')])
def test_parametrize(key, value):
    response_parametrize = requests.get (url = f'{URL}/pokemons', params= {'trainer_id':TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value


def test_change_pokemon_name():
    url = 'https://api.pokemonbattle.ru/v2/pokemons'
    headers = {
        'trainer_token': '9f68bedd420a3ee5251cf9c7b040bfd6',
        'Content-Type': 'application/json'
    }
    payload = {
        "pokemon_id": "206770",
        "name": "Пикачу",
        "photo_id": 2
    }

    response = requests.put(url, headers=headers, json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    try:
        response_data = response.json()
    except json.JSONDecodeError:
        assert False, "Response is not in JSON format"


def test_catch_pokeball():
    url = 'https://api.pokemonbattle.ru/v2/trainers/add_pokeball'
    headers = {
        'trainer_token': '9f68bedd420a3ee5251cf9c7b040bfd6',
        'Content-Type': 'application/json',
        'trainer_id': '19208'
    }
    payload = {
        "pokemon_id": "207505"
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.json()



import requests
def tests_trainers():
  url = 'https://api.pokemonbattle.ru/v2/trainers'
  params = {'trainer_id': '19208'}

response = requests.get( url = 'https://api.pokemonbattle.ru/v2/trainers', params={'trainer_id': '19208'}
)
assert response.status_code == 200
print('Статус код 200: Запрос успешен.')
data = response.json()
trainer_name = 'Алинка'
if trainer_name in data.get('name', 'Алинка'):
 print('Имя тренера присутствует в ответе.')



