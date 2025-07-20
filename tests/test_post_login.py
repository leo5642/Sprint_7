import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure

class TestPostLogin():
    @allure.step('Проверка возможности арторизации курьера')
    def test_authorization(self):
        payload = AuthData.my_login.copy()
        r = requests.post(UrlCollector.login_courier_hand, data=payload)
        assert r.status_code == 200
    
    @pytest.mark.parametrize("missing_field", AuthData.my_login)
    @allure.step('ошибка при не правильном логине или пароле')
    def test_authorization_no_login_or_password(self, missing_field):
        payload = AuthData.my_login.copy()
        payload[missing_field] =  ''

        r = requests.post(UrlCollector.login_courier_hand, data=payload)
        assert r.status_code == 400
    
    @pytest.mark.parametrize("missing_field", AuthData.my_login)
    @allure.step('ошибка при не полных обязательных данных')
    def test_authorization_no_valide_login_or_password(self, missing_field, login_gen):
        payload = AuthData.my_login.copy()
        payload[missing_field] = 'error' + payload[missing_field]

        r = requests.post(UrlCollector.login_courier_hand, data=payload)

        assert 404 == r.status_code
    
    @allure.step('ошибка при авторизации под несуществующим логином')
    def test_non_existent(self):
        payload = AuthData.my_login.copy()
        payload[login] = 'leo564'

        r = requests.post(UrlCollector.login_courier_hand, data=payload)
        assert 400 == r.status_code

    @allure.step('возвращение ид при успешной отправке кода')
    def test_non_existent(self):
        payload = AuthData.my_login.copy()

        r = requests.post(UrlCollector.login_courier_hand, data=payload)
        r = r.json()
        assert r["id"] == 577040


