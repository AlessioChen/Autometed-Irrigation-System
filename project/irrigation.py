from django.core.wsgi import get_wsgi_application
from django.utils import timezone
import time 
import os

from plant.scripts import AirSensor, SoilHumiditySensor, Motor as m 



#----------------- These lines are for allowing to make querys with .py----------------#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
application = get_wsgi_application()
#----------------- --------------------------------------------------------------------#


while True: 
    m.turn_off()
    if SoilHumiditySensor.get_value() < 70: 
        for i in range(0,3):
            m.turn_on()
            time.sleep(0.5)
            m.turn_off()
            time.sleep(1)
            print(SoilHumiditySensor.get_value())
    print(SoilHumiditySensor.get_value())
    m.turn_off()



    
   

