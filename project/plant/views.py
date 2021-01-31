from django.shortcuts import render
from django.http import JsonResponse
from .scripts import Motor
from .scripts import SoilHumiditySensor
from .scripts import AirSensor
from .models import Plant
from datetime import datetime, timedelta, time
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




def graphics(request):

    today = datetime.now().date() 
    end_date = today + timedelta(days = 1)


    context = set_context(today, end_date)

       
    return render(request, 'plant/graphics.html', context)


def update_motor(request):
    motor_status = request.session.get('motor_status','OFF')
    print(motor_status)
    if motor_status == 'OFF' :  #turn on the motor 
        request.session['motor_status'] = 'ON'
        Motor.turn_on()
    else: 
        request.session['motor_status'] = 'OFF'
        Motor.turn_off()

    
    context = {
        'motor_status': motor_status,
    }



    return JsonResponse(context, status =200)



def update_sensors(request):
    
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
            hour_later = timezone.now().replace(minute=0, second=0, microsecond=0)
            now = hour_later - timedelta(hours=1)
            context = set_context(now, hour_later)
        if t == "last_month":
            today = datetime.now().date() + timedelta(days =1)
            one_month_earlier = today - timedelta(days=30)
            context = set_context(one_month_earlier, today)
        
        return JsonResponse(context, status = 200)


    return JsonResponse({"error": "Error!"}, status=400)
  
    
