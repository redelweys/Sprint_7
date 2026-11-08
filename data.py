class Urls:
    BASE_URL = 'https://qa-scooter.education-services.ru'
    COURIER = f'{BASE_URL}/api/v1/courier'
    COURIER_LOGIN = f'{COURIER}/login'
    ORDERS = f'{BASE_URL}/api/v1/orders'
    CANCEL_ORDER = f'{ORDERS}/cancel'