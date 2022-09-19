from twttr import shorten

def test_lower():
    assert shorten("a") == ""
    assert shorten("e") == ""
    assert shorten("i") == ""
    assert shorten("o") == ""
    assert shorten("u") == ""

def test_upper():
    assert shorten("A") == ""
    assert shorten("E") == ""
    assert shorten("I") == ""
    assert shorten("O") == ""
    assert shorten("U") == ""

def test_words():
    assert shorten("1234") == "1234"
    assert shorten("Hello") == "Hll"
    assert shorten("HellO my Name is") == "Hll my Nm s"
    assert shorten("") == ""
    assert shorten("   ") == "   "
    assert shorten("!@#$") == "!@#$"





