from rest_framework import generics

from .models import Investors
from .serializers import InvestorSerializer


class InvestorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Investors.objects.all()
    serializer_class = InvestorSerializer


class InvestorDetailAPIView(generics.RetrieveAPIView):
    queryset = Investors.objects.all()
    serializer_class = InvestorSerializer