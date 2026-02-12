import pytest

with pytest.raises(ValueError, match="invalid"):
    int("abc")
