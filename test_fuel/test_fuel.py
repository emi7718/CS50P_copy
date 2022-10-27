from fuel import gauge, convert
import pytest

def test_num_values():
    assert convert('99/100') == 99
    assert convert('1/100') == 1
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'

def test_exceptions():
    with pytest.raises(ValueError):
        convert('10/2')
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ValueError):
        convert('')
    with pytest.raises(TypeError):
        gauge('cat')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

