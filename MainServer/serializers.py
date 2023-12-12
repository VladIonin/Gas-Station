from rest_framework import serializers
from .models import FuelStation, FuelPrices, Fuel


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelStation
        fields = '__all__'


class PriseSerializer(serializers.ModelSerializer):
    station = StationSerializer(read_only=True)

    class Meta:
        model = FuelPrices
        fields = ['station', 'price']
