from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    total_clicks = models.PositiveBigIntegerField()
    average_clicking_speed = models.FloatField()
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} наклікав {self.total_clicks} разів, з середньою швидкістю {self.average_clicking_speed} кліків на хвилину."
