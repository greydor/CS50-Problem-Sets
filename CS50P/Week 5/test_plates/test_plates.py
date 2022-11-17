from plates import is_valid

def main():
    test_1()
    test_2()
    test_3()
    test_4()

def test_1():
    assert is_valid("A") == False
    assert is_valid("ABCDEFGHI") == False
    assert is_valid("ABCDE") == True

def test_2():
    assert is_valid("12GFRE") == False


def test_3():
    assert is_valid("ABCD0") == False
    assert is_valid("ABC56T") == False
    assert is_valid("123456") == False

def test_4():
    assert is_valid("AB!FGR") == False
    assert is_valid(" frge4") == False
    assert is_valid("ABcde4") == True




if __name__ == "__main__":
    main()
