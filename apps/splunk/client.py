from py_singleton import singleton
from splunklib import client

from django.conf import settings


@singleton
class SplunkClient:
    service: client.Service = None

    def __init__(self):
        self.service = client.connect(
            host=settings.SPLUNK_HOST,
            username=settings.SPLUNK_USERNAME,
            password=settings.SPLUNK_PASSWORD,
            autologin=True
        )

    def push(self, idx, data):
        target = self.service.indexes[idx]
        target.submit(event=data)
