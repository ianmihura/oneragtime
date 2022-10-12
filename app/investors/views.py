from rest_framework import generics

from .models import Investors
from .serializers import InvestorSerializer


class InvestorListCreateAPIView(generics.ListCreateAPIView):
    """
    List all Investors, can create new entries
    """
    queryset = Investors.objects.all()
    serializer_class = InvestorSerializer


class InvestorDetailAPIView(generics.RetrieveAPIView):
    """
    Single Investor detail
    """
    queryset = Investors.objects.all()
    serializer_class = InvestorSerializer
