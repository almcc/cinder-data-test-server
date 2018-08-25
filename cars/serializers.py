from cars.models import Manufacturer
from cars.models import Car
from rest_framework import serializers


class ManufacturerSerializer(serializers.ModelSerializer):
    """Serializer for the Manufacturer model."""

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')


class CarSerializer(serializers.ModelSerializer):
    """Serializer for the Car model."""


    class Meta:
        model = Car
        fields = ('id', 'name', 'created_at', 'updated_at', 'manufacturer')
