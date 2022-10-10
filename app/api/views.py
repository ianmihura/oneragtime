from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """test endpoint"""

    data = request.data
    return Response(data)