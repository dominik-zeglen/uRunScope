from django.db import models
from django.conf import settings


class Training(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=3, decimal_places=2)  # km
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    duration = models.DurationField()
