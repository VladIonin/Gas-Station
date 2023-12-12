from django.contrib import admin
from .models import FuelStation, Fuel, FuelPrices


@admin.register(FuelStation)
class FuelStationAdmin(admin.ModelAdmin):
    list_display = ("station_id", "address")


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ("fuel_id", "name")


@admin.register(FuelPrices)
class FuelPricesAdmin(admin.ModelAdmin):
    list_display = ("station", "fuel", "price", "amount")