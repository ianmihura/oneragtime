from rest_framework import serializers
from .models import Cashcalls


class CashcallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashcalls
        fields = [
            # TODO 'bills',
            # TODO 'investor', 1-1
            'pk',
            'total_amount',
            'IBAN',
            'email_send',
            'date_aded',
            'invoice_status',
        ]
