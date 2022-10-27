from plates import is_valid

def test_two_letters():
    assert is_valid('CS50') == True
    assert is_valid('cs05') == False
    assert is_valid('aa') == True
    assert is_valid('12') == False
    
def test_max_6_chars():
    assert is_valid('ABCDEF') == True
    assert is_valid('a') == False
    assert is_valid('abcdefg') == False

def test_first_two_not_numbers():
    assert is_valid('12abcd') == False
    assert is_valid('as12ed') == False
    assert is_valid('de1234') == True


def test_no_punct():
    assert is_valid('ab.123') == False
