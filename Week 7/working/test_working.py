import pytest
from working import convert

def test_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_time():
    assert convert("12:30 AM to 7 PM") == "00:30 to 19:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
