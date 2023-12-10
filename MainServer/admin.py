from django.contrib import admin
from .models import FuelStation, Fuel, FuelPrices


@admin.register(FuelStation)
class FuelStationAdmin(admin.ModelAdmin):
    list_display = ("Station_ID", "Address")


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ("Fuel_ID", "Name")


@admin.register(FuelPrices)
class FuelPricesAdmin(admin.ModelAdmin):
    list_display = ("Station_ID", "Fuel_ID", "Price", "AmountOfFuel")