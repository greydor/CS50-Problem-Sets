from um import count

def test_0():
    assert count("") == 0
    assert count("umumumumum") == 0
    assert count("john is glum") == 0

def test_1():
    assert count("um hello") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("john is, um, glum") == 1

def test_2():
    assert count("um um!") == 2
