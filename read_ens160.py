import time
import board
import adafruit_ens160
from read_dht20 import check_the_temp

def read_from_ens160():
    # Set up I2C object
    i2c = board.I2C()
    ens = adafruit_ens160.ENS160(i2c)

    # Read ambient temperature to calibrate the sensor
    current_temp, current_humidity = check_the_temp();
    ens.temperature_compensation = (current_temp - 32) * 5/9
    ens.humidity_compensation = current_humidity

    # Validate data being read
    dataAreValid = False
    while (not dataAreValid):
        #print(f"{ens.AQI}  {ens.TVOC}  {ens.eCO2}\n")
        dataAreValid = ens.AQI > 0 and ens.TVOC > 0 and ens.eCO2 > 0
        time.sleep(3)
    
    return ens.AQI, ens.TVOC, ens.eCO2

    # while True:
    #     print("AQI (1-5): ", ens.AQI)
    #     print("TVOC (ppb): ", ens.TVOC)
    #     print("eCO2 (ppm): ", ens.eCO2)
    #     print()

    # # Delay 3 seconds
    #     time.sleep(3)


# def validate_ens_data():
#     dataAreValid = False
#     while (not dataAreValid):
#         readAQI, readTVOC, readECO2 = read_from_ens160()
#         print(f"{readAQI}  {readTVOC}  {readECO2}\n")
#         dataAreValid = readAQI > 0 and readTVOC > 0 and readECO2 > 0
#         #time.sleep(1)

#     return readAQI, readTVOC, readECO2
    
