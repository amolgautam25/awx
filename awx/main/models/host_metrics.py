from django.db import models


class HostMetrics(models.Model):
    hostname = models.CharField(primary_key=True, max_length=30)
    first_automation = models.DateTimeField()
    last_automation = models.DateTimeField()
