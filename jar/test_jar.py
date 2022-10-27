import pytest
from jar import Jar

def test_init():
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0
    jar_1 = Jar()
    assert jar_1.capacity == 12
    jar_1.size = 5
    assert jar_1.size == 5

def test_str():
    jarA = Jar()
    jarA.deposit(5)
    assert jarA.size == 5
    assert str(jarA) == '🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(25)
    jar.deposit(10)
    assert jar.size == 10

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(2)
    jar.deposit(10)
    jar.withdraw(4)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.withdraw(50)

