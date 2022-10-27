import pytest
from working import convert

def test_1():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_2():
    with pytest.raises(ValueError):
       convert('9 to 5')

def test_3():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

def test_4():
    with pytest.raises(ValueError):
        convert('10:66 PM to 128:30 AM')
        convert('10:66 PM to 8:30 AM')

def test_5():
    with pytest.raises(ValueError):
        convert('9 AM to 21:00')

def test_6():
    with pytest.raises(ValueError):
        convert('')
