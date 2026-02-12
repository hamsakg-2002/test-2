# using fixtures
import pytest
@pytest.fixture
def s_list():
    return [1,2,3,4]
@pytest.mark.xfail(reason="Known bug: wrong expected max value")
def test_max_list(s_list):
    assert max([1,2,3,4]) == 2
def test_min_list(s_list):
    assert min([1, 2, 3, 4]) == 1



