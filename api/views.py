from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.amadeus import Amadeus

from .serializers import FlightSearchAPISerializer


class PingAPI(APIView):

    @staticmethod
    def get(request):
        return Response({"data": "pong"}, status=status.HTTP_200_OK)


class FlightPriceAPI(APIView):

    """
    This API returns the cheapest flight between the origin and destination
    """

    @staticmethod
    def get(request):
        data = {
            "org_code": request.GET.get("org_code"),
            "dest_code": request.GET.get("dest_code"),
            "depart_date": request.GET.get("depart_date"),
            "num_adults": int(request.GET.get("num_adults") or 1)
        }

        # We can perform validation checks at the serialization level
        serializer = FlightSearchAPISerializer(data)
        amadeus = Amadeus()
        response = amadeus.get_cheapest_flight(**serializer.data)
        if not response:
            return Response({"message": "Couldn't fetch results"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data)
