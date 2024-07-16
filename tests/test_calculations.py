# Import opertations from operations.py
from calculator.operations import add, multiply,subtract,divide

def test_add():
    # Assert that addition was executed correctly
    assert add(2,2) == 4

def test_subtract():
    # Assert that subtraction was executed correctly
    assert subtract(2,1) == 1

def test_multiply():
    # Assert that multiplication was executed correctly
    assert multiply(2,1) == 2

def test_divide():
    # Assert that division was executed correctly
    assert divide(2,2) == 1