from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import Bills
from api.validators import ValueAllowedValidator


class BillSerializer(serializers.ModelSerializer):
    investment_url = serializers.SerializerMethodField(read_only=True)
    investor_url = serializers.HyperlinkedIdentityField(
        view_name='investor-detail',
        lookup_field='investor_id',
        lookup_url_kwarg='pk')
    fees_type = serializers.CharField(
        validators=[ValueAllowedValidator(['upfront', 'yearly', 'membership'])])

    class Meta:
        model = Bills
        fields = [
            'pk',
            'investor_id',
            'investor_url',
            'investment_id',
            'investment_url',
            'fees_amount',
            'date_added',
            'fees_type',
        ]

    def get_investment_url(self, obj):
        request = self.context.get('request')
        if request is None or obj.investment_id is None:
            return None
        return reverse("investment-detail", kwargs={"pk": obj.investment_id}, request=request)
