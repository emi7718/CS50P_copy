from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('HELLO') == 0

def test_hi():
    assert value('hi') == 20
    assert value('HI') == 20

def test_other():
    assert value('other') == 100
    assert value('OTHER') == 100