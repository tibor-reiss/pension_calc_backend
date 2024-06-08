from decimal import Decimal
from typing import Any, Optional

import pytest
from rest_framework.exceptions import ParseError

from loan.views import validate_decimal, validate_mortgage_term, validate_down_payment


def test_validate_decimal_ok() -> None:
    assert validate_decimal("5") == Decimal(5)


def test_validate_decimal_error() -> None:
    with pytest.raises(ParseError):
        validate_decimal("5a")


@pytest.mark.parametrize(
    "term, expected",
    [
        ("1 year", Decimal(12)),
        ("1 years", Decimal(12)),
        ("2 year", Decimal(24)),
        ("2 years", Decimal(24)),
        ("1 month", Decimal(1)),
        ("1 months", Decimal(1)),
        ("2 month", Decimal(2)),
        ("2 months", Decimal(2)),
    ],
)
def test_validate_mortgage_term_ok(term: str, expected: Decimal) -> None:
    assert validate_mortgage_term(term) == expected


@pytest.mark.parametrize(
    "term, error_str",
    [
        ("", "Invalid mortgage term input"),
        ("1", "Invalid mortgage term input"),
        ("1 yea", "Invalid mortgage term input"),
        ("x years", "Could not parse mortgage term:"),
    ],
)
def test_validate_mortgage_term_error(term: str, error_str: str) -> None:
    with pytest.raises(ParseError) as exc:
        validate_mortgage_term(term)
    assert error_str in str(exc.value.detail)


@pytest.mark.parametrize(
    "down_payment, down_payment_percent, purchase_price, expected",
    [
        ("5000", "", Decimal(10000), Decimal(5000)),
        ("5000", None, Decimal(10000), Decimal(5000)),
        ("0", "", Decimal(10000), Decimal(0)),
        ("0", "20", Decimal(10000), Decimal(0)),
        ("", "20", Decimal(10000), Decimal(2000)),
        (None, "20", Decimal(10000), Decimal(2000)),
    ],
)
def test_validate_down_payment_ok(
    down_payment: str,
    down_payment_percent: str,
    purchase_price: Decimal,
    expected: Decimal,
) -> None:
    assert validate_down_payment(
        down_payment,
        down_payment_percent,
        purchase_price,
    ) == expected


@pytest.mark.parametrize(
    "down_payment, down_payment_percent, purchase_price, error_str",
    [
        ("", "", Decimal(10000), "Missing input down payment"),
        ("", None, Decimal(10000), "Missing input down payment"),
        (None, "", Decimal(10000), "Missing input down payment"),
        (None, None, Decimal(10000), "Missing input down payment"),
        ("", "invalid", Decimal(10000), "Invalid down payment percent input"),
        ("invalid", "20", Decimal(10000), "Invalid down payment input"),
    ],
)
def test_validate_down_payment_error(
    down_payment: Optional[Any],
    down_payment_percent: Optional[Any],
    purchase_price: Decimal,
    error_str: str,
) -> None:
    with pytest.raises(ParseError) as exc:
        validate_down_payment(
            down_payment,
            down_payment_percent,
            purchase_price,
        )
    assert error_str == str(exc.value.detail)
