"""
Models for the pension calculator.
"""

from decimal import Decimal

from django.db import models


TWO_DIGITS = Decimal(10) ** -2


class PensionCalc(models.Model):
    """Pension calc class"""

    monthly_contribution = models.DecimalField(max_digits=10, decimal_places=2)
    yearly_interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    starting_capital = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.DecimalField(max_digits=3, decimal_places=0)
    create_time = models.DateTimeField(auto_now_add=True)

    @property
    def total_capital(self) -> Decimal:
        total = self.starting_capital
        monthly_rate = self.yearly_interest_rate / Decimal(12.0 * 100)
        for _ in range(term * 12):
            total = total * (Decimal(1.0) + monthly_rate) + self.monthly_contribution
        return total
