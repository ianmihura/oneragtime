from rest_framework import serializers
from .models import Investors


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investors
        fields = [
            # 'bills',
            # 'investments',
            # 'cashcall',
            'pk',
            'name',
            'address',
            'credit',
            'phone',
            'email',
        ]