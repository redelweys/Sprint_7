import allure
import requests

from data import Urls


class TestGetOrders:

    @allure.title('В ответе на запрос списка заказов поле orders содержит список')
    def test_get_orders_returns_list(self):
        response = requests.get(Urls.ORDERS, params={'limit': 1}, timeout=10)

        assert response.status_code == 200, response.text
        assert isinstance(response.json()['orders'], list)