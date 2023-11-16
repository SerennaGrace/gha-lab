from addition import add
import pytest

def test_simple():
    assert add(1,2) == 3

def test_str():
    with pytest.raises(ValueError):
        add('one','two')