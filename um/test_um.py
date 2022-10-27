import pytest
from um import count

def test_1():
    assert count('um. um- um,') == 3

def test_2():
    assert count('   um  ') == 1

def test_3():
    assert count('UM') == 1

def test_4():
    assert count('umbrella') == 0