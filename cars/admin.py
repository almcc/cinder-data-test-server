from django.contrib import admin

from .models import Car, Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'manufacturer')
    list_filter = ('year', 'manufacturer')
