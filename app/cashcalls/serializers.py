from rest_framework import serializers
from .models import Cashcalls
from api.validators import ValueAllowedValidator


class CashcallSerializer(serializers.ModelSerializer):
    invoice_status = serializers.CharField(
        validators=[ValueAllowedValidator(['valid', 'sent', 'paid', 'overdue'])])
    invoice_status_edit_url = serializers.HyperlinkedIdentityField(
        view_name='cashcall-status',
        lookup_field='pk')

    class Meta:
        model = Cashcalls
        fields = [
            'pk',
            'total_amount',
            'credit',
            'email_send',
            'date_added',
            'invoice_status',
            'invoice_status_edit_url',
        ]
    

class CashcallStatuserializer(serializers.ModelSerializer):
    invoice_status = serializers.CharField(
        validators=[ValueAllowedValidator(['valid', 'sent', 'paid', 'overdue'])])

    class Meta:
        model = Cashcalls
        fields = ['pk', 'invoice_status']
