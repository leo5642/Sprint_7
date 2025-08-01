import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure
class TestPostOrder():
    @pytest.mark.parametrize("color", AuthData.color)
    @allure.title('можно указать один из цветов')
    def test_authorization_color_black(self, color):
        payload = AuthData.orders.copy()
        payload["color"] = color
        payload = json.dumps(payload)

        with allure.step('отпрака запроса на создание заказа'):
            r = requests.post(UrlCollector.post_order, data=payload)
        assert r.status_code == 201

    @allure.title('можно указать оба цвета')
    def test_authorization_color_crey_and_black(self):
        payload = AuthData.orders.copy()
        payload["color"] = AuthData.color
        payload = json.dumps(payload)

        with allure.step('указание оба цвета при отправке запроса'):
            r = requests.post(UrlCollector.post_order, data=payload)
        assert r.status_code == 201
    
    @allure.title('можно совсем не указывать цвет')
    def test_authorization_color_no(self):
        payload = AuthData.orders.copy()
        payload["color"] = ''
        payload = json.dumps(payload)

        with allure.step('отправка запроса без цвета'):
            r = requests.post(UrlCollector.post_order, data=payload)
        assert r.status_code == 201
    
    @allure.title('Что тело ответа содержит track')
    def test_authorization_response(self):
        payload = AuthData.orders.copy()
        payload["color"] = 'GREY'
        payload = json.dumps(payload)

        with allure.step('наличие праивльного ответа от запроса'):
            r = requests.post(UrlCollector.post_order, data=payload)
        assert r.status_code == 201
        r = r.json()
        assert 'track' in r