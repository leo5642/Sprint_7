import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure

class TestPostCourier():
    @allure.step('Тестирование api /api/v1/courier при успешной регистрации')
    def test_new_courier(self, login_gen):
        payload = login_gen

        r = requests.post(UrlCollector.new_courier_hand, data=payload)
        assert r.status_code == 201
        assert r.json() == {'ok': True}
    
    @allure.step('нельзя создать двух одинаковых курьеров ')
    def test_dabl_courier(self, login_gen):
        payload = login_gen

        requests.post(UrlCollector.new_courier_hand, data=payload)
        r = requests.post(UrlCollector.new_courier_hand, data=payload)
        assert r.status_code == 409
    
    @pytest.mark.parametrize("missing_field, expected_message", AuthData.login)
    @allure.step('если одного из полей нет, запрос возвращает ошибку')
    def test_no_str(self, login_gen, missing_field, expected_message):
        payload = login_gen.copy()
        payload.pop(missing_field)

        r = requests.post(UrlCollector.new_courier_hand, data=payload)
        r = r.json()
        assert r['message'] == expected_message

    @allure.step('если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_too_login(self):
        payload = AuthData.my_login

        r = requests.post(UrlCollector.new_courier_hand, data=payload)
        assert r.status_code == 409
