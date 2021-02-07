from django.shortcuts import render
from django.http import JsonResponse
from .scripts import Motor
from .scripts import SoilHumiditySensor
from .scripts import AirSensor
from .models import Plant, Motor as M 
from datetime import datetime, timedelta
import time
from django.utils import timezone





def set_context(start_date, end_date):

    data = Plant.objects.filter(misurated_time__range=[start_date, end_date])

    air_humidity =[]
    soil_humidity =[]
    air_temperature =[]
    times = []

    for d in data: 
        
        air_humidity.append(d.air_humidity)
        soil_humidity.append(d.soil_humidity)
        air_temperature.append(d.air_temperature)
        times.append(d.misurated_time.strftime("%Y-%m-%d,%H:%M:%S"))
  
    context = {
        "air_humidity": air_humidity,
        "soil_humidity": soil_humidity,
        "air_temperature": air_temperature,
        "times": times
    }

    return context 

def index(request):

    return render(request, 'plant/index.html', {})

def gallery(request):

    return render(request, 'plant/gallery.html', {})


def graphics(request):

    today = datetime.now().date() 
    end_date = today + timedelta(days = 1)


    context = set_context(today, end_date)

       
    return render(request, 'plant/graphics.html', context)


def update_motor(request):
    o = M.objects.all()[0]
  
    if request.is_ajax: 
        #spegni
        if o.status == False:
            o.status = True
            r = 'ON'
            Motor.turn_off()
        #Accendi
        else: 
            o.status = False
            r = 'OFF'
            Motor.turn_on()


        context = {
            'motor_status': r,
        }

        print(r)

        o.save()
    
    return JsonResponse(context, status =200)

def chek_motor_status(request):
    o = M.objects.all()[0]
    if o.status == False: 
        r = 'OFF' 
    else: 
        r = 'ON'

    context = {
        'motor_status': r,
    }



    return JsonResponse(context, status =200)



def update_sensors(request):
    o = M.objects.all()[0]
    if request.is_ajax:
        air_humidity = AirSensor.get_air_humidity()
        soil_umidity = SoilHumiditySensor.get_value()
        air_temperature = AirSensor.get_air_temperature()

       

        context = {
            'air_humidity': air_humidity,
            'soil_humidity': soil_umidity,
            'air_temperature' : air_temperature
        }
        
        #print(context)
        
        return JsonResponse(context, status = 200)


    return JsonResponse({"error": "Error!"}, status=400)

    

def update_graph(request):
 

    if request.is_ajax:
        t = request.POST['type']
        
        if t == "last_hour": 
            hour_earlier = timezone.now().replace(minute=0, second=0, microsecond=0)
            now = hour_earlier + timedelta(hours=1)
          
            context = set_context(hour_earlier, now)
        if t == "last_month":
            today = datetime.now().date() + timedelta(days =1)
            one_month_earlier = today - timedelta(days=30)
            context = set_context(one_month_earlier, today)
        if t == "last_day":
            today = datetime.now().date() + timedelta(days =1)
            earlier  = today - timedelta(days=1)

            context = set_context(earlier, today)
            print(context)
        if t == "last_week":
            today = datetime.now().date() + timedelta(days =1)
            earlier  = today - timedelta(days=7)
            context = set_context(earlier, today)
            
        return JsonResponse(context, status = 200)


    return JsonResponse({"error": "Error!"}, status=400)
  
    
