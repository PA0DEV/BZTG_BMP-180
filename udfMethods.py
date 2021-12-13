#
# name: Phillip Ahlers 
# created:  10.12.2021
# class: ETS2021
#
#
# use:
# - dewPoint: calculate the dewpoint based on humidity and temperature
# - 
# 
# version: 2021_12_10_001
# designed and tested on ESP32 TTGO
# pin conenctions:
# -/-
# 
# used libaries:
# -/-
# ----------------------------------------
#
import math
import time

def dewPoint(temp, humid):
    """
    Calculate the dew point.
    

    :param temp: The temperature measured in °C
    :param humid: The humidity measured in %
    :return: returns the dew point in °C
    """

    humidity = humid / 100
    k2 = 7.5
    k3 = 237.3
    step1 = ((k2 * temp) / (k3 + temp)) + math.log10(humidity)
    step2 = ((k2 * k3) / (k3 + temp)) - math.log10(humidity)
    dewPoint = k3 * (step1 / step2)

    return dewPoint


def smoothMesure(cnt, val, delay = 0):
    """
    Smothen the mesurement. Get "cnt" values, cut off highest and lowest value and get the average.
    
        :param cnt: the number of iterations to be used
        :param val: the mesured value
        :param delay: delay in between the mesurements
        :return: returns the smoothed value of the mesurement
    """
    values = []
    for i in range(cnt):
        values.append(val)
        time.sleep(delay)

    #cut the highest and lowest value
    values.sort()
    values.pop(0)
    values.pop()

    #get the average value
    valLen = len(values)
    valSum = sum(values)
    ret = valSum / valLen

    return ret
