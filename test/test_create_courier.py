import allure
import api
from data import Messages
import pytest



class TestCreateCourier:

    @allure.title('Можно создать курьера с новым логином')
    def test_create_courier_success(self, courier_data):
        response = api.create_courier(courier_data)

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать курьера с занятым логином')
    @pytest.mark.parametrize(
        'password_suffix',
        ['', 'x'],
        ids=['same_data', 'same_login_different_password']
    )
    def test_create_courier_with_existing_login(self, courier_data, registered_courier, password_suffix):
        second_payload = courier_data.copy()
        second_payload['password'] = registered_courier['password'] + password_suffix
        response = api.create_courier(second_payload)

        assert response.status_code == 409, response.text
        assert response.json()['message'] == Messages.LOGIN_TAKEN

    @allure.title('Нельзя создать курьера без поля {missing_field}')
    @pytest.mark.parametrize('missing_field', ['login', 'password', 'firstName'])
    def test_create_courier_without_required_field(self, courier_data, missing_field):
        payload = courier_data.copy()
        del payload[missing_field]

        response = api.create_courier(payload)

        assert response.status_code == 400, response.text
        assert response.json()['message'] == Messages.MISSING_CREATE_DATA
