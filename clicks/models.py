from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    total_clicks = models.PositiveBigIntegerField()
    average_clicking_speed = models.FloatField()
    last_activity = models.DateTimeField(auto_now=True)
