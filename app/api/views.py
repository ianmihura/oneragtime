from rest_framework.decorators import api_view
from rest_framework.response import Response

from investors.serializers import InvestorSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    test endpoint
    """
    serializer = InvestorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response()