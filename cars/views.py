from rest_framework import viewsets

from cars.models import Car, Manufacturer

from .serializers import CarSerializer, ManufacturerSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """View set for Manufacturer model."""

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name',)


class CarViewSet(viewsets.ModelViewSet):
    """View set for Car model."""

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_fields = ('manufacturer',)
    search_fields = ('name',)
    ordering_fields = ('name', 'manufacturer__name')
    ordering = ('name',)
