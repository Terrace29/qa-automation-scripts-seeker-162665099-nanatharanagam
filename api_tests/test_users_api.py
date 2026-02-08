import requests

# def test_get_users_api():
#     response = requests.get("https://jsonplaceholder.typicode.com/users")
#
#     # validate status code
#     assert response.status_code == 200
#
#     #validate response body
#     data = response.json()
#     assert isinstance(data,list)
#     assert len(data) > 0
#     # End of script
#     # start with second script
# def test_get_users():
#     response = requests.get("https://jsonplaceholder.typicode.com/users")
#
#     assert response.status_code == 200
#
#     data = response.json()
#     assert len(data) > 0

def test_user_fields():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()

    assert data["id"] == 1
    assert "email" in data
    assert "username" in data

def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "API testing",
        "body" : "Learning POST API with pytest",
        "userId": 1
    }

    response = requests.post(url,json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "API testing"
    assert data["userId"] == 1

def test_create_post_missing_title():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {

        "body": "Learning POST API with pytest",
        "userId": "abc"
    }

    response = requests.post(url, json=payload)

    assert response.status_code in [201,400]

#GET API WITH HEADRES

def test_get_users_with_headers():
    url = "https://jsonplaceholder.typicode.com/posts"

    headers = {
        "content-Type" : "application/json",
        "Accept": "application/json"

    }

    response = requests.get(url,headers=headers)
    assert response.status_code == 200

def test_post_users_with_headers():
    url = "https://jsonplaceholder.typicode.com/posts"

    headers = {
        "content-Type": "application/json",

    }
    payload = {

        "body": "Learning POST API with pytest",
        "userId": 1
    }
    response = requests.post(url, headers=headers, json = payload)
    assert response.status_code == 201

def test_negative_auth_with_headers():
    url = "https://api.example.com/protected"

    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

import requests

def test_negative_auth_missing_token():
    url = "https://api.example.com/protected"

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 401

def test__pagination_logic():
   page_1_ids = [1,2,3]
   page_2_ids = [4,5,6]

   assert set(page_1_ids).isdisjoint(set(page_2_ids))




