# Raspi Sensor Suite
## Sensor suite setup to send home vital information to user when away from home

To set up this script:
1. Clone the repo to your machine with `wget https://github.com/ElegantDestruction/raspi-ip-pusher.git`
2. Put the get\_ip\_addr.py file in a safe location on your machine
3. Run "update_pbkey.sh" to create the file which contains your pushbullet access token
3. type `crontab -e` and pick an editor (if you've never used it before; nano is the easiest to use)
4. Go to the end of the file, and type `@reboot python /path/to/the/heartbeat_application.py &`
5. Save the file

Alternative to setting up the script to work with the sensor suite heatbeat_application.py file, you can use the get_ip_addr.py file and the send_pushbullet_msg.py to use as an IP address "ping" device

## Note
This script is designed to run when the Raspberry Pi first boots. When this script runs, it will first pause for roughly 45 seconds to allow the system to fully boot and let network manager connect to a network. Only then will the program find the machine's IP address and push it to the Pushbullet account designated with the Access Token entered in the script. Then, every 2 hours, the device will take measurements, and ping the use with information on the home vitals. 

## Sensors:  
[ENS160](https://www.sciosense.com/products/environmental-sensors/ens160-digital-multi-gas-sensor/) 
[DHT20](https://www.adafruit.com/product/5183)  

## Setup:  
[DHT11 and I2C](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)  
[ENS160 Wiring](https://learn.adafruit.com/adafruit-ens160-mox-gas-sensor/pinouts)

Have fun!
