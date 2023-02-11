import time
import board
import adafruit_ens160
from read_dht20 import check_the_temp

def read_from_ens160:
    # Set up I2C object
    i2c = board.I2C()
    ens = adafruit_ens160.ENS160(i2c)
    
    # Read ambient temperature to calibrate the sensor
    current_temp, current_humidity = check_the_temp();
    ens.temperature_compensation = (current_temp - 32) * 5/9
    ens.humidity_compensation = current_humidity
    
    return ens.AQI, ens.TVOC, ens.eCO2

#    while True:
#        print("AQI (1-5): ", ens.AQI)
#        print("TVOC (ppb): ", ens.TVOC)
#        print("eCO2 (ppm): ", ens.eCO2)
#        print()
    
        # Delay 3 seconds
#         time.sleep(3)

