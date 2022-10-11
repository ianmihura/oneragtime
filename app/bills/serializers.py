from rest_framework import serializers
from .models import Bills


class BillSerializer(serializers.ModelSerializer):
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