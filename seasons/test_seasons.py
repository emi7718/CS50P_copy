from seasons import convert_num_to_letter
import pytest

def test_1():
    assert convert_num_to_letter('2020-12-25') == 'Nine hundred seven thousand, two hundred minutes'

def test_2():
    with pytest.raises(SystemExit):
        convert_num_to_letter('10250-25-12')

def test_3():
    with pytest.raises(SystemExit):
        convert_num_to_letter('asd')

