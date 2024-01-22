import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADERS = {'Content-Type': 'application/json'}

def test_get_trainers():
    """
    KTI-1. Get all trainers
    """
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200, 'Unexpected status code'


def test_get_trainers_by_id():
    """
    KTI-2. Get trainer by id
    """
    response = requests.get(url=f'{URL}/trainers', params = {'trainer_id': 3583}, timeout=5)
    assert response.json()['trainer_name'] == 'Anzhalika', ''
