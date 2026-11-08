import pytest
import requests

from data import Urls
from helpers import generate_courier_data
from helpers import generate_courier_data, generate_order_data


@pytest.fixture
def courier_data():
    payload = generate_courier_data()
    yield payload

    credentials = {
        'login': payload['login'],
        'password': payload['password']
    }
    login_response = requests.post(Urls.COURIER_LOGIN, json=credentials, timeout=10)

    if login_response.status_code != 404:
        login_response.raise_for_status()
        courier_id = login_response.json()['id']
        delete_response = requests.delete(f'{Urls.COURIER}/{courier_id}', timeout=10)
        delete_response.raise_for_status()

@pytest.fixture
def registered_courier(courier_data):
    response = requests.post(Urls.COURIER, json=courier_data, timeout=10)
    assert response.status_code == 201, response.text

    return {
        'login': courier_data['login'],
        'password': courier_data['password']
    }

@pytest.fixture
def order_response(colors):
    payload = generate_order_data(colors)
    response = requests.post(Urls.ORDERS, json=payload, timeout=10)
    yield response

    if response.status_code == 201:
        track = response.json().get('track')
        if type(track) is int:
            cancel_response = requests.put(
                Urls.CANCEL_ORDER, params={'track': track}, timeout=10
            )
            assert cancel_response.status_code == 200, cancel_response.text
            assert cancel_response.json() == {'ok': True}