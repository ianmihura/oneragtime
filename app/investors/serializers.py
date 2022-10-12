from rest_framework import serializers
from .models import Investors


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investors
        fields = [
            'pk',
            'name',
            'address',
            'credit',
            'phone',
            'email',
        ]
