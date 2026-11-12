import allure
import api
from data import Messages
import pytest

from helpers import generate_courier_data


class TestLoginCourier:

    @allure.title('Зарегистрированный курьер может войти и получить свой id')
    def test_login_courier_success(self, registered_courier):
        response = api.login_courier(registered_courier)

        assert response.status_code == 200, response.text
        assert type(response.json()['id']) is int

    @allure.title('Вход курьера с неверным полем {wrong_field}')
    @pytest.mark.parametrize('wrong_field', ['login', 'password'])
    def test_login_courier_with_wrong_credentials(self, registered_courier, wrong_field):
        credentials = registered_courier.copy()
        credentials[wrong_field] += 'x'

        response = api.login_courier(credentials)

        assert response.status_code == 404, response.text
        assert response.json()['message'] == Messages.ACCOUNT_NOT_FOUND

    @allure.title('Нельзя войти без поля {missing_field}')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_login_courier_without_required_field(self, registered_courier, missing_field):
        credentials = registered_courier.copy()
        del credentials[missing_field]

        response = api.login_courier(credentials)

        assert response.status_code == 400, response.text
        assert response.json()['message'] == Messages.MISSING_LOGIN_DATA

    @allure.title('Незарегистрированный курьер не может войти')
    def test_login_unregistered_courier(self):
        data = generate_courier_data()
        credentials = {
            'login': data['login'],
            'password': data['password']
        }

        response = api.login_courier(credentials)

        assert response.status_code == 404, response.text
        assert response.json()['message'] == Messages.ACCOUNT_NOT_FOUND
