import pytest

class UrlCollector:
    url_home = 'https://qa-scooter.praktikum-services.ru'

    new_courier_hand = url_home + '/api/v1/courier'
    login_courier_hand = url_home + '/api/v1/courier/login'
    delete_courier_hand = url_home + '/api/v1/courier/:id'
    post_order = url_home + '/api/v1/orders' 
