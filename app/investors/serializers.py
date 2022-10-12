from rest_framework import serializers
from .models import Investors


class InvestorSerializer(serializers.ModelSerializer):
    bills_url = serializers.HyperlinkedIdentityField(
        view_name='bill-investor',
        lookup_field='pk',
        lookup_url_kwarg='investor_id')

    class Meta:
        model = Investors
        fields = [
            'pk',
            'name',
            'address',
            'credit',
            'phone',
            'email',
            'bills_url',
        ]
