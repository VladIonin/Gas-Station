from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from GasStation.settings import FUEL_TYPE_MAPPING
from .models import FuelPrices, FuelStation, Fuel
from MainServer.serializers import PricesSerializer, InfoSerializer


@api_view(['GET'])
def get_stations_by_fuel(request):
    fuel = request.GET.get('fuel', None)
    try:
        prices = FuelPrices.objects.filter(fuel=FUEL_TYPE_MAPPING[fuel])
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = PricesSerializer(prices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
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


@api_view(['POST'])
def set_station(request):
    station_id = request.data.get('id', None)
    address = request.data.get('address', None)
    data = request.data.get('data', [])

    if not station_id:
        return Response({'error': 'Station ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    station, created = FuelStation.objects.get_or_create(station_id=station_id, defaults={'address': address})

    if address:
        station.address = address
        station.save()

    for details in data:
        fuel_name = details.get('fuel', None)
        price = details.get('price', None)
        amount = details.get('amount', None)

        if fuel_name and price is not None:
            fuel_instance, _ = Fuel.objects.get_or_create(name=fuel_name)
            fuel_prices, created = FuelPrices.objects.get_or_create(
                station=station,
                fuel=fuel_instance,
                defaults={'price': price, 'amount': amount}
            )

            if not created:
                fuel_prices.price = price
                if amount is not None:
                    fuel_prices.amount = amount
                fuel_prices.save()

    data = FuelPrices.objects.filter(station=station)
    serializer = InfoSerializer({
        'station': station,
        'data': data,
    })
    return Response(serializer.data, status=status.HTTP_200_OK)
