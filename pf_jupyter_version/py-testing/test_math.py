from calc import *

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2
    
def test_sub_positive_numbers():
    assert subtract(5, 3) == 2
    
def test_sub_negative_numbers():
    assert subtract(-5, -3) == -2
    
def test_multiply_positive():
    assert multiply(6, 4) == 24
    
def test_multiply_negative():
    assert multiply(-7, -3) == 21