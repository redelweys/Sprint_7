import allure
import api



class TestGetOrders:

    @allure.title('В ответе на запрос списка заказов поле orders содержит список')
    def test_get_orders_returns_list(self):
        response = api.get_orders(limit=1)

        assert response.status_code == 200, response.text
        assert isinstance(response.json()['orders'], list)
