from rest_framework import generics

from .models import Investments
from .serializers import InvestmentSerializer


class InvestmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Investments.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Investments.objects.all()
    serializer_class = InvestmentSerializer