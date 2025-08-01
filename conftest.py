import json
import requests
import pytest
from locators.data import AuthData
from locators.url_and_hand import UrlCollector
import string 
import random


@pytest.fixture(scope="class")
def login_gen():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    yield payload
    r = requests.post(UrlCollector.login_courier_hand, data=payload)
    payload = r.json()
    requests.delete(UrlCollector.delete_courier_hand, data=payload)

