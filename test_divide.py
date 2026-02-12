import pytest
def divide(a,b):
    return a/b
def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)
def test_divide_by_zero_message():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(5, 0)

