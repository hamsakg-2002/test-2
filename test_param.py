import pytest
@pytest.mark.parametrize(
    "a,b,result",
    [
        (2,3,5),
        (1,2,3),
        pytest.param(4,5,9, marks = pytest.mark.skip(reason="SKIPPING THIS CASE"))])
def test_add(a,b,result):
    assert a+b == result

