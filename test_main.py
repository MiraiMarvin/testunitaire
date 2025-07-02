
from main import addition
from main import seconde_to_minute
from main import list_converter


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0

def test_seconde_to_minute():

    assert seconde_to_minute(120) == "ça fait 2 minute(s)"
    assert seconde_to_minute(60) == "ça fait 1 minute(s)"
    assert seconde_to_minute(0) == "ça fait 0 minute(s)"
    assert seconde_to_minute(180) == "ça fait 3 minute(s)"
    assert seconde_to_minute(300) == "ça fait 5 minute(s)"

def test_list_converter():
    assert list_converter([120, 60, 0]) == ["ça fait 2 minute(s)", "ça fait 1 minute(s)", "ça fait 0 minute(s)"]
    assert list_converter([180, 300]) == ["ça fait 3 minute(s)", "ça fait 5 minute(s)"]
    assert list_converter([]) == []  # Test with an empty list
