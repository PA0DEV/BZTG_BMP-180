#
# Name: Phillip Ahlers 
# Datum:  16.11.2021
# Klasse: ETS2021
#
# Version: 1.0.0 
#-------------------------------------------------------
##Imports##
import st7789py
from bmp180 import BMP180                               # import bmp180 libary
from machine import Pin, SoftI2C, SoftSPI               # create an I2C bus object accordingly to the port you are using
import time                                             # import time module
from romfonts import vga1_16x16 as font

#-------------------------------------------------------
# ## Initialize Sensor and Bus ##
busSensor =  SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)   # create Software I2C Bus on Pins 22, 21
bmp180 = BMP180(busSensor)                                    # initiate sensor
bmp180.oversample_sett = 2                              # set oversample
bmp180.baseline = 101325                                # set pressure baseline (1013,25hPa)

#-------------------------------------------------------
##Initialize Display and Bus ##
busDisplay = SoftSPI(
    baudrate = 20000000,
    polarity = 1,
    phase = 0,
    sck = Pin(18, Pin.OUT),
    mosi = Pin(19, Pin.OUT),
    miso = Pin(13, Pin.OUT)
)
tft = st7789py.ST7789(
    busDisplay,
    135,
    240,
    reset = Pin(23, Pin.OUT),
    dc = Pin(16, Pin.OUT),
    cs = Pin(5, Pin.OUT),
    rotation = 1,
    backlight = Pin(4, Pin.OUT)
)

#-------------------------------------------------------
## Loop
while True:                                             # infinite loop
    print("\n\n")
    temp = bmp180.temperature                           # read sensor temperature
    p = (bmp180.pressure) / 100                         # read sensor pressure (hPa)


    output1 = str("%d C" %(temp)) # print temperature
    output2 = str("%d hPa" %p)
    # print(output)

    if temp < 23:
        tft.fill(st7789py.BLUE)
    else:
        tft.fill(st7789py.RED)
    tft.text(font,output1, 10, 10, color=st7789py.WHITE, background=st7789py.BLACK)
    tft.text(font,output2, 10, 50, color=st7789py.WHITE, background=st7789py.BLACK)

    time.sleep(10)                                      # delay 10s