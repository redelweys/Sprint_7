import allure
import requests

from data import Urls


@allure.step('Создать курьера')
def create_courier(payload):
    return requests.post(Urls.COURIER, json=payload, timeout=10)


@allure.step('Войти как курьер')
def login_courier(credentials):
    return requests.post(Urls.COURIER_LOGIN, json=credentials, timeout=10)


@allure.step('Удалить курьера')
def delete_courier(courier_id):
    return requests.delete(f'{Urls.COURIER}/{courier_id}', timeout=10)


@allure.step('Создать заказ')
def create_order(payload):
    return requests.post(Urls.ORDERS, json=payload, timeout=10)


@allure.step('Отменить заказ')
def cancel_order(track):
    return requests.put(Urls.CANCEL_ORDER, params={'track': track}, timeout=10)


@allure.step('Получить список заказов')
def get_orders(limit=1):
    return requests.get(Urls.ORDERS, params={'limit': limit}, timeout=10)
