def validate_response(response):
    if response.get("status") == 'ACTIVE':
       return "pass"
    else:
        return "fail"
def test_validate_response_active_status():
    response = {
        "id": 2001,
        "name": "Test User",
        "status": "ACTIVE"
    }
    result = validate_response(response)
    assert result == "pass"
def test_validate_response_inactive_status():
    response = {
        "id": 2002,
        "name": "Test User"
    }
    result = validate_response(response)
    assert result == "fail"