from rest_framework.decorators import api_view
from rest_framework.response import Response
from GasStation.settings import FUEL_TYPE_MAPPING
from .models import FuelPrices
from .serializers import PriseSerializer


@api_view(['GET'])
def stations_by_fuel(request):
    fuel_type = request.query_params.get('fuel')

    if fuel_type not in FUEL_TYPE_MAPPING:
        return Response({'error': 'Invalid fuel type'}, status=400)

    mapped_fuel_type = FUEL_TYPE_MAPPING[fuel_type]
    prices = FuelPrices.objects.filter(fuel_id=mapped_fuel_type)
    serializer = PriseSerializer(prices, many=True)
    return Response(serializer.data)
