from django.shortcuts import render
from django.http import JsonResponse
#from .scripts import motor
#from .scripts import SoilHumiditySensor
#from .scripts import AirSensor
from .models import Plant



def index(request):

    return render(request, 'plant/index.html', {})



def graphics(request):
    data = Plant.objects.all()
    air_humidity =[]
    soil_humidity =[]
    air_temperature =[]
    times = []
    for d in data: 
        air_humidity.append(d.air_humidity)
        soil_humidity.append(d.soil_humidity)
        air_temperature.append(d.air_temperature)
        times.append(d.misurated_time.strftime("%Y-%m-%d,%H:%M:%S"))
        #times.append(d.misurated_time)
    
    context = {
        "air_humidity": air_humidity,
        "soil_humidity": soil_humidity,
        "air_temperature": air_temperature,
        "times": times
    }

       
    return render(request, 'plant/graphics.html', context)


def update_motor(request):
    # Get a session value, setting a default if it is not present ('off')
    motor_status = request.session.get('motor_status','ON')

    if motor_status == 'OFF' :  #turn on the motor 
        request.session['motor_status'] = 'ON'
        #motor.turn_on()
    else: 
        request.session['motor_status'] = 'OFF'
        #motor.turn_off()

    
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
        
        print(context)
        
        return JsonResponse(context, status = 200)


    return JsonResponse({"error": "Error!"}, status=400)

    



