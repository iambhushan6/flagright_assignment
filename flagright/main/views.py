import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as resp_status
# Create your views here.


@api_view(["GET"])
def test_api_view(request):

    if request.method == "GET":
        return Response({"data": "Welcome"})