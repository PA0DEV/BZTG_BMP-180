#
# Name: Phillip Ahlers 
# Datum:  16.11.2021
# Klasse: ETS2021
#
# Version: 1.1.3 
#-------------------------------------------------------
##Imports##
import st7789py                                         # import display libary
from bmp180 import BMP180                               # import bmp180 libary for temp. sensor
from machine import Pin, SoftI2C, SoftSPI               # imports for Board connections (pins and bus)
from time import sleep                                  # import time module for loop sleep
from romfonts import vga2_16x16 as font                 # import the font for the display
import bh1750


#-------------------------------------------------------
##initialize sensor and bus ##
busSensor =  SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)   # instantiate Software I2C Bus on Pins 22, 21
bmp180 = BMP180(busSensor)                                    # instantiate sensor object
bmp180.oversample_sett = 2                                    # set oversample
bmp180.baseline = 101325                                      # set pressure baseline NN (1013,25hPa)
lightSens = bh1750.BH1750(busSensor)

#-------------------------------------------------------
## initialize display and bus ##
busDisplay = SoftSPI(                               # instantiate software spi bus
    baudrate = 20000000,
    polarity = 1,
    phase = 0,
    sck = Pin(18, Pin.OUT),
    mosi = Pin(19, Pin.OUT),
    miso = Pin(13, Pin.OUT)
)
tft = st7789py.ST7789(                              # instantiate display object
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
## define LED setup

ledRed = Pin(25, Pin.OUT)
ledGreen = Pin(27, Pin.OUT)
ledYellow = Pin(26, Pin.OUT)

#========================================================

## loop
while True:
    # print("\n\n")
    temp = bmp180.temperature                           # read sensor temperature
    p = (bmp180.pressure) / 100                         # read sensor pressure (hPa)
    light = lightSens.luminance(bh1750.BH1750.ONCE_HIRES_1)

    output1 = str("%d \xF8C     " %(temp))                       # create format String for temperature
    output2 = str("%d hPa     " %p)                          # create format string for air-pressure
    output3 = str("%d lux     " %light)

    # if temp < 25:
    #     tft.fill(st7789py.GREEN)                        # fill display and show green led
    #     ledGreen.value(1)
    #     ledYellow.value(0)
    #     ledRed.value(0)
        
    # elif temp < 27:
    #     tft.fill(0xFBE0)                       # fill display and show yellow led
    #     ledGreen.value(0)
    #     ledYellow.value(1)
    #     ledRed.value(0)
        
    # else:                                               # fill display and show red led
    #     tft.fill(st7789py.RED)
    #     ledGreen.value(0)
    #     ledYellow.value(0)
    #     ledRed.value(1)
        

                       
    # print the temperature string on the display
    tft.text(font, output1, 10, 10, color=st7789py.WHITE, background=st7789py.BLACK)
    # print the air-pressure string on the display
    tft.text(font, output2, 10, 50, color=st7789py.WHITE, background=st7789py.BLACK)

    tft.text(font, output3, 10, 90, color=st7789py.WHITE, background=st7789py.BLACK)

    # sleep(0.1)                                           # delay 10s