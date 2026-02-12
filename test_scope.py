import pytest
@pytest.fixture(scope = "class")
def numbers():
    return [1,2,3,4]
class TestMath:
   def test_max(self,numbers):
        assert max(numbers) == 4
   def test_sum(self,numbers):
        assert sum(numbers) == 10


