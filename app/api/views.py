from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    """
    List basic endpoints.
    """
    return Response({
        "bill-list": reverse('bill-list', request=request),
        "cashcall-list": reverse('cashcall-list', request=request),
        "investment-list": reverse('investment-list', request=request),
        "investor-list": reverse('investor-list', request=request),
    })
