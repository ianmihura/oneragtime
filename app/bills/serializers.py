from wsgiref.validate import validator
from rest_framework import serializers
from .models import Bills
from api.validators import ValueAllowedValidator


class BillSerializer(serializers.ModelSerializer):
    fees_type = serializers.CharField(
        validators=[ValueAllowedValidator(['upfront', 'yearly', 'membership'])])

    class Meta:
        model = Bills
        fields = [
            # 'investments',
            # 'investor',
            'pk',
            'investor_id',
            'investment_id',
            'fees_amount',
            'date_added',
            'fees_type',
        ]
