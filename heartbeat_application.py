#!/usr/bin/env python3

# Attempt to import python 3.0, fall back if necessary
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

# Import os for bash call and time for sleep functionality
import os
import time

# Import functions from subfiles
from read_dht20 import check_the_temp
from send_pushbullet_msg import send_pushbullet_msg
from get_ip_addr import get_ip_addr
from read_ens160 import read_from_ens160
iPHeader = "Apollo IP"
vitalsHeader = "House Vitals"

#Configurable delay times
bootDelay = 1 #seconds
transmissionDelay = 5 #seconds, 2 hours

#Boot delay
time.sleep(bootDelay)

#1 get initial IP address, record it, and send it to pushbullet
previousIP = get_ip_addr()
print("made it here")
send_pushbullet_msg(previousIP, iPHeader)

#2 begin looping
while True:
    #2a Check IP address. If different from prev, resend it in dedicated message
    newIP = get_ip_addr()
    if newIP != previousIP:
        previousIP = newIP
        send_pushbullet_msg(previousIP, iPHeader)

    #2b Get Relative Temp and Humidity
    currentTemp, currentHumidity = check_the_temp()

    #2c Get Air Quality data
    currentAQI, currentTVOC, currentCO2 = read_from_ens160()

    #2d Package all data into a message for pushbullet, and send
    tempString = f"'Temp: {currentTemp:0.2f} degF\n'"
    humidityString = f"'RH: {currentHumidity:0.2f} percent\n'"
    aQIString = f"'AQI: {currentAQI} (1-5)\n'"
    tVOCString = f"'TVOC: {currentTVOC} ppb\n'"
    eCO2String = f"'eCO2: {currentCO2} ppm\n'"
    fullVitalsMessage = tempString + humidityString + aQIString + tVOCString + eCO2String
    send_pushbullet_msg(fullVitalsMessage, vitalsHeader)

    #2e Sleep for a configurable amount of time
    time.sleep(transmissionDelay)