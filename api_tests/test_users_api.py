import requests

def test_get_users_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    # validate status code
    assert response.status_code == 200

    #validate response body
    data = response.json()
    assert isinstance(data,list)
    assert len(data) > 0
    # End of script
    # start with second script
