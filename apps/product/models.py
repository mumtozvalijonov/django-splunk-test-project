from django.db import models

from uuid import uuid4

from .tasks import product2splunk


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def to_splunk_format(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'price': self.price
        }

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        result = super().save(*args, **kwargs)
        product2splunk.delay(self.id)
        return result
