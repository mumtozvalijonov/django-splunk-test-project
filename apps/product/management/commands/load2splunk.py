from django.core.management.base import BaseCommand

from apps.product.tasks import product2splunk
from apps.product.models import Product


class Command(BaseCommand):
    help = 'Sends products to splunk'

    def handle(self, *args, **options):
        for product in Product.objects.all():
            product2splunk(product.id)
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded product {product}'))
