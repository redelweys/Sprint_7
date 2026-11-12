class Urls:
    BASE_URL = 'https://qa-scooter.education-services.ru'
    COURIER = f'{BASE_URL}/api/v1/courier'
    COURIER_LOGIN = f'{COURIER}/login'
    ORDERS = f'{BASE_URL}/api/v1/orders'
    CANCEL_ORDER = f'{ORDERS}/cancel'


class Messages:
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    MISSING_LOGIN_DATA = 'Недостаточно данных для входа'
    LOGIN_TAKEN = 'Этот логин уже используется'
    MISSING_CREATE_DATA = 'Недостаточно данных для создания учетной записи'
