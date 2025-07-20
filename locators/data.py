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

    ordersid = '568068'
