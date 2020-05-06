import pytest
from Code import unittesting

def test_answer():
    assert unittesting.func(6) == 12
    assert unittesting.func(2) == 4