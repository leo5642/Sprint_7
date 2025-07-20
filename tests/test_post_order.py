import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure
class TestPostOrder():
    @pytest.mark.parametrize("color", AuthData.color)
    @allure.step('можно указать один из цветов')
    def test_authorization_color_black(self, color):
        payload = AuthData.orders.copy()
        payload["color"] = color
        payload = json.dumps(payload)

        r = requests.post(UrlCollector.post_order, data=payload)
        assert r.status_code == 201

    @allure.step('можно указать оба цвета')
    def test_authorization_color_crey_and_black(self):
        payload = AuthData.orders.copy()
        payload["color"] = AuthData.color
        payload = json.dumps(payload)

        r = requests.post(UrlCollector.post_order, data=payload)
        assert r.status_code == 201
    
    @allure.step('можно совсем не указывать цвет')
    def test_authorization_color_no(self):
        payload = AuthData.orders.copy()
        payload["color"] = ''
        payload = json.dumps(payload)

        r = requests.post(UrlCollector.post_order, data=payload)
        assert r.status_code == 201
    
    @allure.step('Что тело ответа содержит track')
    def test_authorization_response(self):
        payload = AuthData.orders.copy()
        payload["color"] = 'GREY'
        payload = json.dumps(payload)

        r = requests.post(UrlCollector.post_order, data=payload)
        r = r.json()
        assert 'track' in r