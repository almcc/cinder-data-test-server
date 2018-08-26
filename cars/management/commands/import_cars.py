import csv

from django.core.management.base import BaseCommand

from cars.models import Car, Manufacturer


def _get_or_create_manufacturer(manufacturer_name):
    try:
        return Manufacturer.objects.get(name=manufacturer_name)
    except Manufacturer.DoesNotExist:
        manufacturer = Manufacturer(name=manufacturer_name)
        manufacturer.save()
        return manufacturer


class Command(BaseCommand):
    """Import car management command."""

    help = 'TODO'

    def add_arguments(self, parser):
        """Dataset argument."""
        parser.add_argument('dataset', type=str)

    def handle(self, dataset, **options):
        """Command handler."""
        print(dataset)

        with open(dataset, newline='\n') as csvfile:
            car_reader = csv.reader(csvfile, delimiter=',')
            for year, make, model in car_reader:
                manufacturer = _get_or_create_manufacturer(make)
                car = Car(name=model, year=year, manufacturer=manufacturer)
                car.save()
                print('Created {0} {1} {2}'.format(year, model, make))
