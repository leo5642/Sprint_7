import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure

class TestGetOrder():
    @allure.title('в тело ответа возвращается список заказов')
    def test_my_order_in_order(self):
        with allure.step('Отправка запроса за списком и проверка наличие заказа в списке'):
            r = requests.get(UrlCollector.post_order+ '/track?t=' + f'{AuthData.id_ordersid}')
        assert r.status_code == 200
        r = r.json()
        assert r["order"]["track"] == AuthData.id_ordersid
