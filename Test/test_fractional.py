import pytest
from Code import factorial_challenge

def test_answer():
    assert factorial_challenge.function(3) == "The factorial of" + " " + str(3) + " " + "=" + " " + str(6)
    assert factorial_challenge.function(4) == "The factorial of" + " " + str(4) + " " + "=" + " " + str(24)
    assert factorial_challenge.function(0) == "The factorial of 0 is 1"
    