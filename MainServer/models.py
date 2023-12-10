from django.db import models


class FuelStation(models.Model):
    Station_ID = models.AutoField(primary_key=True)
    Address = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.Station_ID}] {self.Address}"


class Fuel(models.Model):
    Fuel_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class FuelPrices(models.Model):
    Station_ID = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    Fuel_ID = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    AmountOfFuel = models.PositiveIntegerField()
