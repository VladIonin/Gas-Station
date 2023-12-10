from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from MainServer.models import FuelStation, Fuel, FuelPrices

class StationsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Создаем тестовые данные
        self.station1 = FuelStation.objects.create(Station_ID=1, Address="Адрес 1")
        self.station2 = FuelStation.objects.create(Station_ID=2, Address="Адрес 2")
        self.fuel92 = Fuel.objects.create(Name="92")
        self.fuel95 = Fuel.objects.create(Name="95")
        self.price1_92 = FuelPrices.objects.create(
            Station_ID=self.station1, Fuel_ID=self.fuel92, Price=44.09, AmountOfFuel=43360
        )
        self.price1_95 = FuelPrices.objects.create(
            Station_ID=self.station1, Fuel_ID=self.fuel95, Price=47.67, AmountOfFuel=50149
        )
        self.price2_92 = FuelPrices.objects.create(
            Station_ID=self.station2, Fuel_ID=self.fuel92, Price=44.49, AmountOfFuel=56531
        )
        self.price2_95 = FuelPrices.objects.create(
            Station_ID=self.station2, Fuel_ID=self.fuel95, Price=47.85, AmountOfFuel=81209
        )

    def test_get_stations_by_fuel_type(self):
        url = reverse("get_stations_by_fuel")
        response = self.client.get(url, {"fuel": "92"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # Проверьте, что станции вернулись с правильной информацией

    def test_post_set_station(self):
        url = reverse("set_station")
        data = {
            "ID": 3,
            "Address": "Новый адрес",
            "fuel_data": [
                {"Name": "92", "Price": 45.0, "AmountOfFuel": 60000},
                {"Name": "95", "Price": 48.0, "AmountOfFuel": 70000},
            ],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Проверьте, что станция добавлена в базу данных

    def test_get_station_info(self):
        url = reverse("get_station_info", kwargs={"id": self.station1.Station_ID})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверьте, что информация о станции вернулась правильно

    def test_report(self):
        url = reverse("generate_report")
        response = self.client.get(url, {"type": "some_type"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)