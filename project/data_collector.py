
from django.core.wsgi import get_wsgi_application
from django.utils import timezone
import time 
import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
application = get_wsgi_application()

from plant.models import *

# TO DO take misurations every tot seconds and save it in database 


osservation = Plant()


osservation.soil_humidity = 5
osservation.air_humidity = 5
osservation.air_temperature = 5
osservation.misurated_time = timezone.now()

osservation.save()

  

d = Plant.objects.all()
for p in d: 
    print(p.get_time())