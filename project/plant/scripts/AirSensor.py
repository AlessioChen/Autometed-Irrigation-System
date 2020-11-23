import time
import busio
import board
from adafruit_htu21d import HTU21D

# Create library object using our Bus I2C port

i2c = busio.I2C(board.SCL, board.SDA)
sensor = HTU21D(i2c)

def get_air_temperature():
    return sensor.temperature
    # print("\nTemperature: %0.1f C" % sensor.temperature)
    # print("Humidity: %0.1f %%" % sensor.relative_humidity)
    #     time.sleep(1)

def get_air_humidity():
    return sensor.relative_humidity