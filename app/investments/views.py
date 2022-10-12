from rest_framework import generics

from .models import Investments
from .serializers import InvestmentSerializer


class InvestmentListCreateAPIView(generics.ListCreateAPIView):
    """
    List all Investments, can create new entries
    """
    queryset = Investments.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentDetailAPIView(generics.RetrieveAPIView):
    """
    Single Investment detail
    """
    queryset = Investments.objects.all()
    serializer_class = InvestmentSerializer
