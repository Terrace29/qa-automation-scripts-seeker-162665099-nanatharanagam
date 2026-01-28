
def is_less_than_100(num):
    return num < 100
def test_num_less_than():
    assert is_less_than_100(50)

#function +loop

def is_postive(num):
    return num > 0
def test_postive_num():
    numbers = [2,4,5,6]

    for num in numbers:
        assert is_postive(num)

#string contains

def is_string_present(text,word):
    return word in text
def test_string_contains():
    assert is_string_present("Python Programming","Python")

def is_greater_than_0(num):
    return num > 0
def test_num_greater_than():
    assert is_greater_than_0(50)

def has_min_length(text):
    return len(text) > 3
def test_min_length():
    assert has_min_length("Automation")

def is_valid_age(age):
    return age >= 20 and age <= 50
def test_valid_age():
    assert is_valid_age(20)

def is_number_less_than(num):
    return num < 100
def test_is_number_less_than():
    assert is_number_less_than(100)

def is_string_qa(text):
    return "QA" in text
def test_is_string_qa():
    assert is_string_qa("QA test")

def is_age_between(age):
    return age > 18 and age < 20
def test_is_age():
    value = [19]

    for age in value:
        assert is_age_between(age)

def is_string_length(text):
    return len(text) > 5
def test_is_string_length():
    texts = ["QA automation","QA Engineering"]
    for text in texts:
        assert is_string_length(text)



