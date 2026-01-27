import pytest
@pytest.mark.parametrize("value",[1,5,10])
def test_value_greater(value):
    assert value > 0

@pytest.mark.parametrize("a,b",
                         [
                             (10,10),
                             (5,5),
                             (3,3)
                         ]
)
def test_equal_check(a,b):
    assert a == b

@pytest.mark.parametrize("text,word",
                         [
                             ("QA Automation","QA"),

                            ("Automation Testing","Automation")
                         ]
)
def test_string_word(text,word):
    assert word in text

@pytest.mark.parametrize("status",[("Active"),("Inactive")])
def test_status_val(status):

    if status == "Active":
        assert status == "Active"
    else:
        assert status != ""

@pytest.mark.parametrize("texts",[("QA","python","Automation")])
def test_my_strings(texts):

    for text in texts:
        assert len(text) > 0
