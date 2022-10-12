from datetime import datetime
from django.db.models import Sum
from rest_framework import generics, status
from rest_framework.response import Response

from bills.models import Bills
from investors.models import Investors
from .models import Cashcalls
from .serializers import CashcallSerializer, CashcallStatuserializer


class CashcallListAPIView(generics.ListAPIView):
    """
    List all Cashcalls
    """
    queryset = Cashcalls.objects.all()
    serializer_class = CashcallSerializer


class CashcallDetailAPIView(generics.RetrieveAPIView):
    """
    Single Cashcall detail
    """
    queryset = Cashcalls.objects.all()
    serializer_class = CashcallSerializer


class CashcallStatusAPIView(generics.RetrieveUpdateAPIView):
    """
    Single Cashcall status, also used to update invoice_status
    """
    queryset = Cashcalls.objects.all()
    serializer_class = CashcallStatuserializer


class CashcallCreateAPIView(generics.CreateAPIView):
    """
    Create single Cashcall
    Given an investor_id, will create the Cashcall for all their bills
    """
    queryset = Cashcalls.objects.all()
    serializer_class = CashcallSerializer

    def get_cashcall(self, investor_id):
        """
        Returns cashcall dict based on investor's bills
        Used to create cashcall with CashcallSerializer
        """
        investor = Investors.objects.get(id=investor_id)
        return {
            "total_amount": Bills.objects.filter(investor_id=investor_id).aggregate(sum=Sum('fees_amount'))['sum'],
            "credit": investor.credit,
            "email_send": investor.email,
            "date_added": datetime.now(),
            "invoice_status": 'valid'
        }

    def post(self, request, *args, **kwargs):
        # get cashcall data for investor_id
        data = self.get_cashcall(kwargs['investor_id'])
        serializer = self.get_serializer(data=data)

        # default code of generic view
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
