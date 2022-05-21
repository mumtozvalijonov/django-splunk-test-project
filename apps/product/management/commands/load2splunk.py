from django.core.management.base import BaseCommand, CommandError

from apps.splunk.client import SplunkClient
from apps.product.models import Product


class Command(BaseCommand):
    help = 'Sends products to splunk'

    def handle(self, *args, **options):
        splunk_client = SplunkClient()
        for product in Product.objects.all():
            data = {
                'id': str(product.id),
                'name': product.name,
                'price': product.price
            }
            splunk_client.push('main', data)
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded product {product}'))