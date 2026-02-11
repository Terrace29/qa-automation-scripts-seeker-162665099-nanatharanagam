#Mock Test Data Management & Reusability practice

import requests
import uuid
#Dyanamic data(Make test stable)
def test_create_user_dynamic_data():
    url = "https://api.example.com/users"

    unique_email = f"user_{uuid.uuid4()}@example.com"

    payload = {
        "name": "Test user",
        "email": unique_email
    }

    response = requests.post(url,json=payload)

    assert response.status_code == 201
    assert response.json()["email"] == unique_email
#Parametrization
import requests
import pytest

@pytest.mark.parametrize("bad email",[
    "",
    "invalidemail",
    "test@",
])
def test_invalid_user_email(bad_email):
    url = "https://api.example.com/users"

    payload = {
        "name": "Test user",
        "email": bad_email
    }

    response = requests.post(url,json=payload)

    assert response.status_code == 400

import uuid
#centralized Testdata (keep payloads in one place)
#test_data/user_payloads.py
def valid_user_payload():
    return {
        "name": "Test user",
        "email": f"user_{uuid.uuid4()}@example.com"
    }
def invalid_user_payload_missing_email():

    return {
        "name": "Test user"
    }
#valid_user_payload
import requests
from test_data.user_payloads import valid_user_payload, invalid_user_payload_missing_email

def test_create_user_success():
    url = "https://api.example.com/users"

    payload = valid_user_payload()

    response = requests.post(url,json=payload)
    assert response.status_code == 201



 def test_create_user_missing_email():
     url = "https://api.example.com/users"
     payload = invalid_user_payload_missing_email()

     response = requests.post(url, json=payload)
     assert response.status_code == 400

 #Cleanup(Avoid polluting DB / environment)


import requests
import uuid

def test_create_user_and_cleanup():
    base_url = "https://api.example.com/users"
    unique_email = f"user_{uuid.uuid4()}@example.com"

    payload = {
        "name": "Test user",
        "email": unique_email
    }

    create_resp = requests.post(base_url,json=payload)
    assert create_resp.status_code == 201

    user_id = create_resp.json()["id"]

    delete_resp = requests.delete(f"{base_url}/{user_id}")
    assert delete_resp.status_code in [200,204]











