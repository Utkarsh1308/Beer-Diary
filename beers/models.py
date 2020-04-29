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

    alcohol = models.FloatField(default=5)
    hoppy = models.FloatField(default=20)
    floral = models.FloatField(default=10)
    herbal= models.FloatField(default=5)
    spicy = models.FloatField(default=10)
    malty = models.FloatField(default=5)
    burnt = models.FloatField(default=5)
    sweet = models.FloatField(default=10)
    sour = models.FloatField(default=5)
    bitter = models.FloatField(default=10)
    dry = models.FloatField(default=10)
    linger = models.FloatField(default=5)

    def __str__(self):
        return self.name

    def flavors(self):
        return [self.alcohol, self.hoppy, self.floral, self.herbal, self.spicy,
                self.malty, self.burnt, self.sweet, self.sour, self.bitter,
                self.dry, self.linger]
