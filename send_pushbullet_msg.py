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

def send_pushbullet_msg(message, title):
    with open('pushbullet_key.txt') as file_handler:
        pushbullet_auth = file_handler.read().strip(' \n')

    bash_command = "curl --silent -u \"\"\"" + pushbullet_auth + "\"\":\" -d type=\"note\" -d body=" + message + " -d title=\"" + title + "\" 'https://api.pushbullet.com/v2/pushes'"
    os.system(bash_command)

