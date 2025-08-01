import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure

class TestPostLogin():
    @allure.title('Проверка возможности арторизации курьера')
    def test_authorization(self):
        payload = AuthData.my_login.copy()
        with allure.step('Отправка запроса на авторизацию'):
            r = requests.post(UrlCollector.login_courier_hand, data=payload)
        assert r.status_code == 200
        r = r.json()
        assert r["id"] == AuthData.id_login
    
    @pytest.mark.parametrize("missing_field", AuthData.my_login)
    @allure.title('ошибка при не правильном логине или пароле')
    def test_authorization_no_login_or_password(self, missing_field):
        payload = AuthData.my_login.copy()
        payload[missing_field] =  ''
        with allure.step('Отправка запроса авторизации с не правильным логином или паролем'):
            r = requests.post(UrlCollector.login_courier_hand, data=payload)
        assert r.status_code == 400
        r = r.json()
        assert r['message'] == AuthData.error_login_400
    
    @pytest.mark.parametrize("missing_field", AuthData.my_login)
    @allure.title('ошибка при не полных обязательных данных')
    def test_authorization_no_valide_login_or_password(self, missing_field, login_gen):
        payload = AuthData.my_login.copy()
        payload[missing_field] = 'error' + payload[missing_field]
        with allure.step('отправка запроса без логинв или пароля'):
            r = requests.post(UrlCollector.login_courier_hand, data=payload)
        assert 404 == r.status_code
        r = r.json()
        assert r['message'] == AuthData.error_login_404
    
    @allure.title('ошибка при авторизации под несуществующим логином')
    def test_non_existent(self):
        payload = AuthData.my_login.copy()
        payload[login] = 'leo564'
        with allure.step('отправка запроса с неправльным логином'):
            r = requests.post(UrlCollector.login_courier_hand, data=payload)
        assert 400 == r.status_code
        r = r.json()
        assert r['message'] == AuthData.error_login_404

    @allure.title('возвращение ид при успешной отправке кода')
    def test_non_existent(self):
        payload = AuthData.my_login.copy()
        with allure.step('Ответ от ручки об номере аккаунта'):
            r = requests.post(UrlCollector.login_courier_hand, data=payload)
        assert r.status_code == 200
        r = r.json()
        assert r["id"] == AuthData.id_login


