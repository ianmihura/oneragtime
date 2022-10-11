from rest_framework import generics

from .models import Bills
from .serializers import BillSerializer


class BillListAPIView(generics.ListAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillSerializer


class BillInvetsorAPIView(generics.ListAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillSerializer

    # TODO get: show only bills of given investor
    # TODO post (empty payload): create cashcall for given group of bills


class BillDetailAPIView(generics.RetrieveAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillSerializer