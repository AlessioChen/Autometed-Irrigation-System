from django.shortcuts import render
from django.http import JsonResponse
#from .scripts import motor
#from .scripts import GrowHumiditySensor
#from .scripts import SoilHumiditySensor


def index(request):

    return render(request, 'plant/index.html', {})


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
        # Get a session value, setting a default if it is not present (0)   
        t = request.session.get('air_humidity', 0)
        t2 = request.session.get('soil_umidity', 0)

        air_humidity = get_air_humidity(t)
        soil_umidity = get_soil_humidity(t2)
        air_temperature = get_air_temperature(t)

        request.session['air_humhidity'] = air_humidity
        request.session['soil_umidity'] = soil_umidity


        context = {
            'air_humidity': air_humidity,
            'soil_humidity': soil_umidity,
            'air_temperature' : air_temperature
        }
        return JsonResponse(context, status = 200)

    return JsonResponse({"error": "Error!"}, status=400)

    


def get_air_humidity(value):
    # return GrowHumiditySensor.get_value()
    return value + 10

def get_soil_humidity(value):
    # return SoilHumiditySensor.get_value()
    return value + 2 

def get_air_temperature(value):
    
    return value + 5

