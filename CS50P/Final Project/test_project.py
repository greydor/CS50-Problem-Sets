from project import extract_filename_data, calculate_test_time, calculate_temp_time_flowrate
import pytest
import pandas as pd

file = pd.read_excel("89ml_m 10c 15 disp2.xlsx", skiprows=6, usecols="A:E")

def test_extract_filename_data():
    assert extract_filename_data("89ml_m 10c 15 disp2.xlsx") == (89, 10, str(15), str(2))
    assert extract_filename_data("89 10 15 2.xlsx") == (89, 10, str(15), str(2))
    assert extract_filename_data("89ml_m 10c 15 disp2 trial2.xlsx") == (89, 10, str(15), str(2))
    assert extract_filename_data("89ml_m 10c.xlsx") == ("","","","")
    assert extract_filename_data("") == ("","","","")
    assert extract_filename_data("ABCml_m ABCc 15 disp2.xlsx") == ("","","","")
    assert extract_filename_data("89ml_m 10c 15 disp2.pdf") == ("","","","")
    assert extract_filename_data("ml_m c 15 disp2.xlsx") == ("","","","")

def test_calculate_temp_time_flowrate():
    assert calculate_temp_time_flowrate(10, 20, 600, 100) == 10
    assert calculate_temp_time_flowrate(10, 20, 1200, 100) == 20
    with pytest.raises(TypeError):
        calculate_temp_time_flowrate("", 20, 600, 100)
    with pytest.raises(TypeError):
        calculate_temp_time_flowrate("A", 20, "B", 100)
    assert calculate_temp_time_flowrate(10, 10, 600, 100) == 0
    assert calculate_temp_time_flowrate(10, 20, 0, 100) == 0

def test_calculate_test_time():
    assert calculate_test_time(file) == pd.Timestamp('2022-07-13 10:51:34')
    with pytest.raises(TypeError):
        calculate_test_time(1)
    with pytest.raises(TypeError):
        calculate_test_time("")