from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from GasStation.settings import FUEL_TYPE_MAPPING
from .models import FuelPrices, FuelStation
from MainServer.serializers import *


@api_view(['GET'])
def get_stations_by_fuel(request):
    fuel = request.GET.get('fuel', None)
    try:
        prices = FuelPrices.objects.filter(fuel=FUEL_TYPE_MAPPING[fuel])
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = PricesSerializer(prices, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_station_info(request):
    station_id = request.GET.get('id', None)
    try:
        station = FuelStation.objects.get(pk=station_id)
    except FuelStation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = FuelPrices.objects.filter(station=station)
    serializer = InfoSerializer({
        'station': station,
        'data': data,
    })
    return Response(serializer.data)
