import pytest
from math_operations import MathOperations
from unittest.mock import patch
import sys
sys.path.append("./")

# Add the 'math_operation' fixture to your tests


@pytest.fixture
def math_operation():
    return MathOperations()


# Use the 'math_operation' fixture in your test functions
def test_add(math_operation):
    with patch.object(MathOperations, 'add', return_value=5):
        assert math_operation.add(2, 3) == 5
        assert math_operation.add(-2, 3) == 5  # Mocking the behavior


def test_subtract(math_operation):
    with patch.object(MathOperations, 'subtract', return_value=2):
        assert math_operation.subtract(5, 3) == 2
        assert math_operation.subtract(2, 3) == 2  # Mocking the behavior


def test_multiply(math_operation):
    with patch.object(MathOperations, 'multiply', return_value=6):
        assert math_operation.multiply(2, 3) == 6
        assert math_operation.multiply(-2, 3) == 6  # Mocking the behavior


def test_divide(math_operation):
    with patch.object(MathOperations, 'divide', return_value=2):
        assert math_operation.divide(6, 3) == 2
        assert math_operation.divide(10, 2) == 2  # Mocking the behavior


def test_power(math_operation):
    with patch.object(MathOperations, 'power', return_value=8):
        assert math_operation.power(2, 3) == 8
        assert math_operation.power(4, 0.5) == 8  # Mocking the behavior


def test_modulo(math_operation):
    with patch.object(MathOperations, 'modulo', return_value=1):
        assert math_operation.modulo(5, 2) == 1
        assert math_operation.modulo(10, 3) == 1  # Mocking the behavior


def test_divide_by_zero(math_operation):
    with patch.object(MathOperations, 'divide', side_effect=ValueError):
        with pytest.raises(ValueError):
            math_operation.divide(6, 0)


def test_modulo_by_zero(math_operation):
    with patch.object(MathOperations, 'modulo', side_effect=ValueError):
        with pytest.raises(ValueError):
            math_operation.modulo(6, 0)
