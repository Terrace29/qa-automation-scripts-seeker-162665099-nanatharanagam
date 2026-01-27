def test_addition():
    assert 2+3 == 5

def test_string_check():
    actual = "QA automation"
    expected = "QA automation"
    assert actual == expected

def test_numbers_equal():
    a = 10
    b= 10
    assert a == b

def test_string_check_word():
    text = "QA Automation"
    assert "QA" in text

def test_value_greater():
    a = 2
    assert a > 0

def test_postive_number():
    value = 5
    if value > 0:
        assert True
    else:
        assert False

def test_status_active():
    status = "active"
    if status == "active":
        assert True
    else:
        assert False

def test_multiple_condition():

    value = 10
    assert 1 < value <= 100

def test_all_numbers_positive():
    numbers = [2,4,16,8]

    for num in numbers:
        if num <= 100:
            assert True
        else:
            assert False

def test_string_list():
    texts = ["QA","Python","SQL","Reporting"]

    for text in texts:
        assert "thon" in texts or "Report"

def test_loop():
    values = [2,3,4,5]

    for val in values:
        if val >= 0:
            assert True
        else:
            assert False







