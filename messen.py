from bmp180 import BMP180
from machine import Pin, SoftI2C                       # create an I2C bus object accordingly to the port you are using
import time
#bus = I2C(1, baudrate=100000)           # on pyboard
bus =  SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)   # on esp8266
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325




while True:
    print("\n\n")
    temp = bmp180.temperature
    p = (bmp180.pressure) / 100

    print("Temperature: %d °C" %temp)
    print("Pressure: %d hPa" %p)
    
    time.sleep(10)
    