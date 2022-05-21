from config.celery import app
from apps.splunk.client import SplunkClient


@app.task
def product2splunk(product_id):
    from .models import Product
    product = Product.objects.filter(id=product_id).first()
    if product:
        splunk_client = SplunkClient()
        splunk_client.push('main', product.to_splunk_format())
