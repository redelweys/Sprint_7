import allure
import pytest


class TestCreateOrder:

    @allure.title('Создание заказа: {param_id}')
    @pytest.mark.parametrize(
        'colors',
        [['BLACK'], ['GREY'], ['BLACK', 'GREY'], None],
        ids=['black', 'grey', 'both_colors', 'no_color']
    )
    def test_create_order_returns_track(self, order_response):
        assert order_response.status_code == 201, order_response.text
        assert type(order_response.json().get('track')) is int, order_response.text