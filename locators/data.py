import pytest
import requests
import random
import string

class AuthData:
    login = [
        ("login", "Недостаточно данных для создания учетной записи"),
        ("password", "Недостаточно данных для создания учетной записи"),
    ]
    
    my_login = {
        "login": "leo5642",
        "password": "1234"
    }

    orders = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": "BLACK"
    }

    color = ['BLACK', 'CREY']
    id_login = 577040
    id_ordersid = 568068

    error_register_409 = 'Этот логин уже используется. Попробуйте другой.'
    error_login_400 = "Недостаточно данных для входа"
    error_login_404 = "Учетная запись не найдена"
