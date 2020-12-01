
from django.core.wsgi import get_wsgi_application
from django.utils import timezone
import time 
import os
from plant.models import *
from plant.scripts import AirSensor, SoilHumiditySensor


#----------------- This lines are for allowing to make querys with .py----------------#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
application = get_wsgi_application()
#----------------- --------------------------------------------------------------------#



osservation = Plant()

# Every minute it read the sensord and add data into database 

while True: 
    osservation.soil_humidity = SoilHumiditySensor.get_value()
    osservation.air_temperature = AirSensor.get_air_temperature()
    osservation.air_humidity = AirSensor.get_air_humidity()
    osservation.misurated_time = timezone.now()

    osservation.save()
    time.sleep(1)

# TODO check the sensors values to activate/deactivate motor 

  

# d = Plant.objects.all()
# for p in d: 
#     print(p.get_time())