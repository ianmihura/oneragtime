from rest_framework import serializers
from .models import Investments


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = [
            # 'bill', # 1-1
            'pk',
            'investor_id', # fk / url
            'startup_name',
            'invested_amount',
            'percentage_fees',
            'date_added',
            'fees_type',
        ]