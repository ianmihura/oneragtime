from rest_framework import serializers
from .models import Investments
from api.validators import ValueAllowedValidator


class InvestmentSerializer(serializers.ModelSerializer):
    investor_url = serializers.HyperlinkedIdentityField(
        view_name='investor-detail',
        lookup_field='investor_id',
        lookup_url_kwarg='pk')
    fees_type = serializers.CharField(
        validators=[ValueAllowedValidator(['upfront', 'yearly'])])

    class Meta:
        model = Investments
        fields = [
            # 'bill', # 1-1
            'pk',
            'investor_id',  # fk
            'investor_url',
            'startup_name',
            'invested_amount',
            'percentage_fees',
            'date_added',
            'fees_type',
        ]
