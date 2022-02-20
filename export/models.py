from django.db import models
import datetime

class People(models.Model):
    signup = models.DateTimeField(default=datetime.date.today)
    points = models.IntegerField(default=0)
    name = models.CharField(max_length=50, blank=False, null=False)