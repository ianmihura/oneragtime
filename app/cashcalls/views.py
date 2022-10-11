from rest_framework import generics

from .models import Cashcalls
from .serializers import CashcallSerializer


class CashcallListAPIView(generics.ListAPIView):
    queryset = Cashcalls.objects.all()
    serializer_class = CashcallSerializer


class CashcallDetailAPIView(generics.RetrieveAPIView):
    queryset = Cashcalls.objects.all()
    serializer_class = CashcallSerializer


class CashcallStatusAPIView(generics.RetrieveAPIView):
    queryset = Cashcalls.objects.all()
    serializer_class = CashcallSerializer

    # TODO get: return only status field
    # TODO update: update status field