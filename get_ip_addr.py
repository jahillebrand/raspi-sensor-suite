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

# Abstract away variables
repeat = True
wait_time = 1 #45
pushbullet_auth = "o.qtFf5pm2aBzc1HMKEAeVMSUkhd14k9sR"
message_title = "Raspi IP"
ip_prev = ""
iteration_count = 0 # Want a heartbeat every 3rd iteration (1.5 hrs)

# Begin Program, attempt to grab system IP
time.sleep(wait_time)
while repeat:
    try:
        ip_address = str(urlopen('http://ip.42.pl/raw').read()).replace("'", '').replace('b','')
        #repeat = False

        if ip_address != ip_prev:
            # Declare Bash command 
            bash_command = "curl --silent -u \"\"\"" + pushbullet_auth + "\"\":\" -d type=\"note\" -d body=" + ip_address + " -d title=\"" + message_title + "\" 'https://api.pushbullet.com/v2/pushes'"
            # Call Bash Command
            os.system(bash_command)

            # Set new IP address
            ip_prev = ip_address
        else:
            if iteration_count > 2:
                # Poll for current temperature
                print("Attempting Temp Read\n")
                from read_dht20 import check_the_temp
                current_temp, current_humidity = check_the_temp()
                print(current_temp)
                print(current_humidity)
                # Create Body of message
                message_body = f"'Heartbeat\nCurrent Temp: {current_temp:0.2f}\nCurrent RH: {current_humidity:0.2f}\n'"
                # Declare Heartbeat command
                bash_command = "curl --silent -u \"\"\"" + pushbullet_auth + "\"\":\" -d type=\"note\" -d body=" + message_body + " -d title=\"" + message_title + "\" 'https://api.pushbullet.com/v2/pushes'"
                print(bash_command)
                # Call bash command
                os.system(bash_command)

                iteration_count = 0
                time.sleep(2)#1800
            else:
                iteration_count = iteration_count + 1
                time.sleep(2)#1800
    except ImportError:
        time.sleep(5)


