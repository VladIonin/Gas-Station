from django.db import models


class FuelStation(models.Model):
    station_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.station_id}] {self.address}"


class Fuel(models.Model):
    fuel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FuelPrices(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    amount = models.PositiveIntegerField(default=0)
