from calculator.operations import add, multiply,subtract,divide

def test_add():
    assert add(2,2) == 4

def test_subtract():
    assert subtract(2,1) == 1

def test_multiply():
    assert multiply(2,1) == 2

def test_divide():
    assert divide(2,2) == 1