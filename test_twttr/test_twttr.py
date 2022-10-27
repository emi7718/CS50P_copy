from twttr import shorten

def testing_no_punct_no_numbers():
    assert shorten('CASITA') == 'CST'
    assert shorten('dictionary') == 'dctnry'

def testing_numbers():
    assert shorten('-1') == '-1'
    assert shorten ('0') == '0'

def testing_punctuation():
    assert shorten(',') == ','
    assert shorten('.') == '.'
    
