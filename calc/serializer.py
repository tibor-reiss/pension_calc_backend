"""
Helpers for communication via REST.
"""

from rest_framework import serializers

from calc.models import PensionCalc


class PensionCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = PensionCalc
        fields = (
            "id",
            "monthly_contribution",
            "yearly_interest_rate",
            "starting_capital",
            "term",
            "create_time",
            "total_capital",
        )
