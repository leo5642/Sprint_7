import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure

class TestGetOrder():
    @allure.step('в тело ответа возвращается список заказов')
    def test_my_order_in_order(self):
        r = requests.get(UrlCollector.post_order+ '/track?t=' + AuthData.ordersid)
        assert r.status_code == 200