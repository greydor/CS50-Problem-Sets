from seasons import minutes


def test_valid():
    assert minutes("2022-08-09") == "Zero minutes"
    assert minutes("2021-08-09") == "Five hundred twenty-five thousand, six hundred minutes"

