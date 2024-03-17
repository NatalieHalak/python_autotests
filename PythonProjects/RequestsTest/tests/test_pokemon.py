import requests
import pytest

URL='https://api.pokemonbattle.me'

def test_status_code():
    response = requests.get(f'{URL}/trainers', params={"trainer_id":2031})
    assert response.status_code == 200

def test_part_of_body(): 
    response = requests.get(f'{URL}/trainers', params={"trainer_id":2031}, headers={"trainer_token":"b6fb96a1fb451a35821eef8835b6e4b1"})
    assert response.json()['trainer_name'] == 'День'