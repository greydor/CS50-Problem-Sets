import fuel
import pytest


def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("5/0")

def test_convert():
    assert fuel.convert("1/3") == 33
    assert fuel.convert("99/100") == 99

def test_convert_value():
    with pytest.raises(ValueError):
        fuel.convert("cat/mouse")

def test_convert_value2():
    with pytest.raises(ValueError):
        fuel.convert("5/4")
    with pytest.raises(ValueError):
        fuel.convert("99")
    with pytest.raises(ValueError):
        fuel.convert("6.778/2.312")

def test_gauge():
    assert fuel.gauge(33) == "33%"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"

