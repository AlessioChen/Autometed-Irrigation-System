from django.shortcuts import render
# Create your views here.


def index(request):
     
     # Get a session value, setting a default if it is not present ('off')
    motor_status = request.session.get('motor_status','off')

    if motor_status == 'off' :  #turn on the motor 
        request.session['motor_status'] = 'on'
    else: 
        request.session['motor_status'] = 'off'

    
    context = {
        'motor_status': motor_status,
    }



    return render(request, 'plant/index.html', context )