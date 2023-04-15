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

def get_ip_addr():
    try: 
        ip_address = str(urlopen('http://ip.42.pl/raw').read()).replace("'", '').replace('b','')
    except ImportError:
        ip_address = "999"

    # Return IP address
    return ip_address