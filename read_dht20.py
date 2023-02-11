import time
import smbus

# Returns temperature, humidity (-1 for both if error)
def check_the_temp():

    # DHT20 Default source address
    DHT20_ADDR = 0x38
    
    STATUS_CMD = 0x71
    DATA_CMD = 0xAC

    DATA_VAL_1 = 0x33
    DATA_VAL_2 = 0x00
    BYTE_1 = 1
    BYTE_7 = 7
    
    
    # Create i2cbus object, pause for init
    i2cbus = smbus.SMBus(1)
    time.sleep(0.5)
    
    # Read for positive sensor status
    data = i2cbus.read_i2c_block_data(DHT20_ADDR, STATUS_CMD, BYTE_1)
    if (data[0] | 0x08) == 0:
        print('Initialization Error: Returning')
        return -1,-1
    
    # Send command to recieve data, pause 100 msecs
    i2cbus.write_i2c_block_data(DHT20_ADDR, DATA_CMD, [DATA_VAL_1, DATA_VAL_2])
    time.sleep(0.1)
    
    # Read in the data from the sensor
    data = i2cbus.read_i2c_block_data(DHT20_ADDR, STATUS_CMD, BYTE_7)
    
    # Process recieved temperature and humidity data
    temp_count = ((data[3] & 0x0F) << 16) + (data[4] << 8) + data[5]
    humid_count = ((data[3] & 0xF0) >> 4) + (data[1] <<12) + (data[2] << 4)
    
    # Convert raw count values to human-readable
    hr_temperature = (200 * float(temp_count)) / (2**20 - 50)
    hr_humidity = (100 * float(humid_count)) / 2**20
    
    # Retvals
    return hr_temperature, hr_humidity


    # Display for debugging
    # print(hr_temperature)
    # print(hr_humidity)



#read_temp,read_humid = check_the_temp()
#print('Printing from call')
#print(read_temp)
#print(read_humid)
