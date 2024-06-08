"""
Views for the pension calculator.
"""

import logging
from decimal import Decimal, InvalidOperation
from typing import Any, Optional

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from calc.models import PensionCalc
from calc.serializer import PensionCalcSerializer


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(),
    ],
)
LOGGER = logging.getLogger(__name__)
# pylint: disable=logging-fstring-interpolation


def validate_decimal(input_str: str) -> Decimal:
    try:
        return Decimal(input_str)
    except InvalidOperation:
        raise ParseError(f"Failed to convert {input_str} to Decimal")


def validate(request: Request) -> PensionCalc:
    """Single point of user input validation"""
    monthly_contribution = validate_decimal(request.data.get("monthly_contribution"))
    yearly_interest_rate = validate_decimal(request.data.get("yearly_interest_rate"))
    starting_capital = validate_decimal(request.data.get("starting_capital"))
    term = validate_decimal(request.data.get("term"))
    return PensionCalc(
        monthly_contribution=monthly_contribution,
        yearly_interest_rate=yearly_interest_rate,
        starting_capital=starting_capital,
        term=term,
    )


@api_view(
    [
        "GET",
    ]
)
def latest_calcs(_request: Request) -> Response:
    pensions = PensionCalc.objects.all().order_by("-create_time")
    serializer = PensionCalcSerializer(pensions, many=True)
    return Response(serializer.data)


@api_view(
    [
        "POST",
    ]
)
def generate_calc(request: Request) -> Response:
    try:
        pension = validate(request)
        pension.save()
        return Response({})
    except ParseError as e:
        LOGGER.error(e)
        return Response({}, status=400)
