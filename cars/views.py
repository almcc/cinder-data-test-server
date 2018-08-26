from rest_framework import viewsets

from cars.models import Car, Manufacturer

from .serializers import CarSerializer, ManufacturerSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """View set for Manufacturer model."""

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at', 'updated_at')
    ordering = ('name',)


class CarViewSet(viewsets.ModelViewSet):
    """View set for Car model."""

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_fields = ('manufacturer', 'year')
    search_fields = ('name', 'year')
    ordering_fields = ('name', 'year', 'created_at', 'updated_at', 'manufacturer__name')
    ordering = ('name',)
