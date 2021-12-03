#
# Name: Phillip Ahlers 
# Datum:  5.10.2021
# Klasse: ETS2021
#
# Version: 1.0.0 
# Aufgabe: 
#Die Luftfeuchte in einem Kellerraum soll gemessen werden. 
#Steigt die Luftfeuchte zu hoch, so soll eine Alarmierung stattfinden

import math

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


# # Eingaben der Parameter
# temp = 20                  # Eingabe Temperatur in °C
# humidPercent = 45      # Eingabe Luftfeuchte in %


# humidity = humidPercent / 100   # Umrechnung % in ganze Zahl

# # Gaskonstanten des Wassers
# k2 = 7.5
# k3 = 237.3


# #berechnung des Taupunktes
# step1 = ((k2 * temp) / (k3 + temp)) + math.log10(humidity)
# step2 = ((k2 * k3) / (k3 + temp)) - math.log10(humidity)
# dewPoint = k3 * (step1 / step2)

# print("\nTemperatur: {} \u00b0C\nLuftfeuchtigkeit: {} %\nTaupunkt: {} \u00b0C".format(round(temp, 2), round(humidPercent, 2), round(dewPoint, 2)))
