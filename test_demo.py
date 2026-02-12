import pytest
@pytest.fixture(scope= "class")
def numbers():
    return [1,2,3]
class TestMath:
  def test_sum(self,numbers):
        assert sum([1,2,3]) == 6
   def test_max(self, numbers):
    assert max([1,2,3]) == 3


