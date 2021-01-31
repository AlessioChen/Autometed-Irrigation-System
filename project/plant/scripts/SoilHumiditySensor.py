import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import RPi.GPIO as GPIO #


def get_value():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)


    # Create the ADC object using the I2C bus
    ads = ADS.ADS1015(i2c)

    # Create single-ended input on channel 0
    chan = AnalogIn(ads, ADS.P3)

  

    humidityPercent = (3.3-chan.voltage)/2.4*100#Soil Humidity Percentage



    
    return humidityPercent


