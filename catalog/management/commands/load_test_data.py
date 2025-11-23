from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Load test data for catalog app'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Loading fixtures...')
        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')

        self.stdout.write(self.style.SUCCESS('Test data loaded successfully'))