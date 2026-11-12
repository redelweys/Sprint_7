import random
import string
from datetime import date, timedelta


def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_courier_data():
    return {
        'login': generate_random_string(),
        'password': generate_random_string(),
        'firstName': 'Mr. Courier'
    }

def generate_order_data(colors):
    payload = {
        'firstName': 'Анна',
        'lastName': 'Тестова',
        'address': 'Москва, Тестовая улица, 10',
        'metroStation': '4',
        'phone': '+7 900 000 00 00',
        'rentTime': 2,
        'deliveryDate': (date.today() + timedelta(days=1)).isoformat(),
        'comment': 'Учебный заказ Sprint_7'
    }
    if colors is not None:
        payload['color'] = colors
    return payload