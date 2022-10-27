from numb3rs import validate

def test_numbers():
    assert validate('0.0.0.0') == True
    assert validate('0.0.0.255') == True
    assert validate('0.0.255.0') == True
    assert validate('0.255.0.0') == True
    assert validate('255.0.0.0') == True


def test_numbers2():
    assert validate('0.0.0.256') == False
    assert validate('0.0.300.0') == False
    assert validate('0.257.0.0') == False
    assert validate('258.0.0.0') == False
    assert validate('cat') == False
    assert validate('10.10.10.255.10') == False

