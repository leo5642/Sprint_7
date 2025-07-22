import json
import requests
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import pytest
import allure

class TestPostCourier():
    @allure.title('Тестирование api /api/v1/courier при успешной регистрации')
    def test_new_courier(self, login_gen):
        payload = login_gen

        with allure.step('регистрациия через ручку со случайными данными'):
            r = requests.post(UrlCollector.new_courier_hand, data=payload)
        assert r.status_code == 201
        assert r.json() == {'ok': True}
    
    @allure.title('нельзя создать двух одинаковых курьеров ')
    def test_dabl_courier(self, login_gen):
        payload = login_gen

        with allure.step('Регистрация'):
            requests.post(UrlCollector.new_courier_hand, data=payload)
        with allure.step('Пoпытка Зарегистрировать теже данные'):
            r = requests.post(UrlCollector.new_courier_hand, data=payload)
        assert r.status_code == 409
        r = r.json()
        assert r['message'] == AuthData.error_register_409
    
    @pytest.mark.parametrize("missing_field, expected_message", AuthData.login)
    @allure.title('если одного из полей нет, запрос возвращает ошибку')
    def test_no_str(self, login_gen, missing_field, expected_message):
        payload = login_gen.copy()
        payload.pop(missing_field)

        with allure.step('отправка запроса без наличия важных полей'):
            r = requests.post(UrlCollector.new_courier_hand, data=payload)
        assert r.status_code == 400
        r = r.json()
        assert r['message'] == expected_message

    @allure.title('если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_too_login(self):
        payload = AuthData.my_login

        with allure.step('отправка на создание аккаунта с уже существующим логином'):
            r = requests.post(UrlCollector.new_courier_hand, data=payload)
        assert r.status_code == 409
        r = r.json()
        assert r['message'] == AuthData.error_register_409
