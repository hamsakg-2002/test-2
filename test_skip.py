import pytest
@pytest.mark.parametrize(
    "a,b,result",
    [
        (1, 2, 3),
        pytest.param(2, 3, 5, marks=pytest.mark.skip(reason="Skipping this case")),
        (3, 4, 7),
    ]
)
def test_add(a, b, result):
    assert a + b == result
