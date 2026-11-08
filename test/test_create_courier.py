import allure
import requests
import pytest

from data import Urls


class TestCreateCourier:

    @allure.title('Можно создать курьера с новым логином')
    def test_create_courier_success(self, courier_data):
        response = requests.post(Urls.COURIER, json=courier_data, timeout=10)

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать курьера с занятым логином')
    @pytest.mark.parametrize(
        'change_password',
        [False, True],
        ids=['same_data', 'same_login_different_password']
    )
    def test_create_courier_with_existing_login(self, courier_data, change_password):
        first_response = requests.post(Urls.COURIER, json=courier_data, timeout=10)
        assert first_response.status_code == 201, first_response.text

        second_payload = courier_data.copy()
        if change_password:
            second_payload['password'] += 'x'

        response = requests.post(Urls.COURIER, json=second_payload, timeout=10)

        assert response.status_code == 409, response.text
        assert response.json()['message'] == 'Этот логин уже используется'

    @allure.title('Нельзя создать курьера без поля {missing_field}')
    @pytest.mark.parametrize('missing_field', ['login', 'password', 'firstName'])
    def test_create_courier_without_required_field(self, courier_data, missing_field):
        payload = courier_data.copy()
        del payload[missing_field]

        response = requests.post(Urls.COURIER, json=payload, timeout=10)

        assert response.status_code == 400, response.text
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'