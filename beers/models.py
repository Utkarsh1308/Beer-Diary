from django.db import models
from datetime import datetime

# Create your models here.
class Beer(models.Model):
    name = models.CharField(max_length=250)
    brewer = models.CharField(max_length=250)
    date = models.DateTimeField(default=datetime.now)
    price = models.FloatField()
    serving_type = models.CharField(max_length=250)
    rating = models.CharField(max_length=250)
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.name
