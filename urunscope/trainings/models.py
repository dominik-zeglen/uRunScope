from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField


class Training(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=3, decimal_places=2)  # km
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField(blank=True)
    duration = models.DurationField(blank=True)
    track = JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
