from django.shortcuts import render
from django.http import JsonResponse
#from .scripts import motor
#from .scripts import GrowHumiditySensor
#form .scripts import SoilHumiditySensor


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
        t = request.session.get('sensor1_value', 0)
        t2 = request.session.get('sensor2_value', 0)

        sensor1_value = get_sensor_1_value(t)
        sensor2_value = get_sensor_2_value(t2)

        request.session['sensor1_value'] = sensor1_value
        request.session['sensor2_value'] = sensor2_value

        context = {
            'sensor1_value': sensor1_value,
            'sensor2_value': sensor2_value
        }
        return JsonResponse(context, status = 200)

    return JsonResponse({"error": "Error!"}, status=400)

    


def get_sensor_1_value(value):
    # return GrowHumiditySensor.get_value()
    return value + 10

def get_sensor_2_value(value):
    # return SoilHumiditySensor.get_value()
    return value + 2 