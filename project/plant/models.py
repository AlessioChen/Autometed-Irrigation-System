from django.db import models
from datetime import datetime 

# Create your models here.

class Plant(models.Model):

    soil_humidity = models.FloatField()
    air_humidity = models.FloatField()
    air_temperature = models.FloatField()
    misurated_time = models.DateTimeField()

    def get_time(self):
        # here we can format the time 
        return self.misurated_time