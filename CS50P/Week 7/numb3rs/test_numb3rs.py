from numb3rs import validate




def test_not_number():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False
    assert validate("") == False
    assert validate("-1.3.3.3") == False
    assert validate("22.cat.cat.cat") == False

def test_number():
    assert validate("0.0.0.0") == True
    assert validate("22.22.") == False
    assert validate("2222.22.22.22") == False
    assert validate("22.2222.22.22") == False
    assert validate("22.22.2222.22") == False
    assert validate("22.22.22.2222") == False
    assert validate("2") == False
    assert validate("22...") == False
    assert validate("255.255.255.255") == True
    assert validate("75.456.76.65") == False