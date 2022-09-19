from bank import value

def test_punctuation():
    assert value("!@#") == 100
    assert value("     ") == 100

def test_word():
    assert value("why") == 100
    assert value("heLLo") == 0
    assert value("Hola") == 20
    assert value("hello there") == 0

def test_sentence():
    assert value("What's up Amigo?") == 100