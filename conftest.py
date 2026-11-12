import pytest
import api

from helpers import generate_courier_data


@pytest.fixture
def courier_data():
    payload = generate_courier_data()
    yield payload

    credentials = {
        'login': payload['login'],
        'password': payload['password']
    }
    login_response = api.login_courier(credentials)

    if login_response.status_code != 404:
        login_response.raise_for_status()
        courier_id = login_response.json()['id']
        delete_response = api.delete_courier(courier_id)
        delete_response.raise_for_status()

@pytest.fixture
def registered_courier(courier_data):
    response = api.create_courier(courier_data)
    response.raise_for_status()

    return {
        'login': courier_data['login'],
        'password': courier_data['password']
    }

@pytest.fixture
def orders_to_cancel():
    responses = []
    yield responses
    for response in responses:
        if response.status_code == 201:
            track = response.json().get('track')
            if type(track) is int:
                api.cancel_order(track).raise_for_status()
