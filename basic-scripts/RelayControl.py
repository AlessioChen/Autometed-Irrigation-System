import RPi.GPIO as GPIO #provides a class to control the GPIO
import time

in1 = 16 #PIN16, GPIO23

GPIO.setmode(GPIO.BOARD) #GPIO.BOARD use PIN ID to init
                         #GPIO.BCM use GPIO ID to init

GPIO.setup(in1, GPIO.OUT) #set in1 as output digital line

try:
    while True:
        
        #TODO while(growHumidity < percent):
            GPIO.output(in1, False) #Engine ON
            time.sleep(2) #for Testing
            
        #TODO out of While(gH < p)
            GPIO.output(in1, True) #Engine OFF
            time.sleep(2) #for Testing


except KeyboardInterrupt: 
    GPIO.cleanup() #Emergency Engine OFF


