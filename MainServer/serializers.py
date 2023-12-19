from rest_framework import serializers
from .models import FuelStation, FuelPrices, Fuel


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelStation
        fields = ['station_id', 'address']


class PricesSerializer(serializers.ModelSerializer):
    station_id = serializers.ReadOnlyField(source='station.station_id')
    address = serializers.ReadOnlyField(source='station.address')

    class Meta:
        model = FuelPrices
        fields = ['station_id', 'address', 'price']


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    fuel = serializers.ReadOnlyField(source='fuel.name')

    class Meta:
        model = FuelPrices
        fields = ['fuel', 'price', 'amount']


class InfoSerializer(serializers.Serializer):
    station = StationSerializer(read_only=True)
    data = DataSerializer(many=True)
