import pytest
from app import validate_amount, calculate_conversion

def test_validate_amount_positive():
    """Test that a positive amount string is correctly validated."""

    amount_str = '100'
    amount, error = validate_amount(amount_str)
    assert amount == 100.0
    assert error is None


def test_validate_amount_negative():
    """Test that a negative amount string returns an appropriate error."""

    amount_str = '-50'
    amount, error = validate_amount(amount_str)
    assert amount is None
    assert error == "Please enter a positive amount."


def test_calculate_conversion():
    """Test that calculate_conversion returns the correct converted amount."""

    amount = 100
    rate = 1.2
    result = calculate_conversion(amount, rate)
    assert result == 120.0