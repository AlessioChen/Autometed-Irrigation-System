from django.core.wsgi import get_wsgi_application
from django.utils import timezone
import time 
import os

from plant.scripts import AirSensor, SoilHumiditySensor, Motor as m 


#----------------- These lines are for allowing to make querys with .py----------------#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
application = get_wsgi_application()
#----------------- --------------------------------------------------------------------#

from plant.models import *

# Every minute it read the sensord and add data into database 

osservation = Plant()
while True: 
    osservation = Plant()
    osservation.soil_humidity = SoilHumiditySensor.get_value()
    osservation.air_temperature = AirSensor.get_air_temperature()
    osservation.air_humidity = AirSensor.get_air_humidity()
    osservation.misurated_time = timezone.now()

    osservation.save()
    print("SAVE")

    time.sleep(60)

   

