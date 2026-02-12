import pytest
@pytest.fixture
def s_list():
    return [1,2,3,4,5,6]
@pytest.mark.xfail(reason ="known:unknown expected max value")
def test_max_value(s_list):
    assert max([1,2,3,4,5,6]) == 1
def test_min_value(s_list):
    assert min([1,2,3,4,5,6,7]) == 1


