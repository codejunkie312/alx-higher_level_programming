import pytest
import sys
sys.path.append("/Users/anassahimi/Desktop/Study/ALX/alx-higher_level_programming/0x07-python-test_driven_development")
add_integer = __import__('0-add_integer').add_integer

def test_add_integer():
    # Test adding two positive integers
    assert add_integer(1, 2) == 3

    # Test adding two negative integers
    assert add_integer(-1, -2) == -3

    # Test adding zero to zero
    assert add_integer(0, 0) == 0

    # Test adding a large positive integer to 1
    assert add_integer(999999999, 1) == 1000000000

    # Test adding a large negative integer to -1
    assert add_integer(-999999999, -1) == -1000000000

    # Test adding a float and an integer
    assert add_integer(1.0, 2) == 3

    # Test adding an integer and a float
    assert add_integer(1, 2.0) == 3

    # Test adding a float and a float
    assert add_integer(1.5, 2.9) == 3

    # Test adding a float and an integer that sum to a float
    assert add_integer(1.5, 2) == 3

    # Test adding an integer and a float that sum to a float
    assert add_integer(1, 1.5) == 2

    # Test adding a single integer
    assert add_integer(1) == 99

    # Test adding a single float
    assert add_integer(1.4) == 99

    # Test adding a string and an integer
    with pytest.raises(TypeError, match="a must be an integer"):
        add_integer("1", 2)

    # Test adding an integer and a string
    with pytest.raises(TypeError, match="b must be an integer"):
        add_integer(1, "2")

    # Test adding None as an argument
    with pytest.raises(TypeError, match="a must be an integer"):
        add_integer(None)
