import requests
import pytest

@pytest.mark .parametrize("user_id",[1,2,3])
def test_get_single_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == user_id

def test_invalid_users():

    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    assert response.status_code == 404
