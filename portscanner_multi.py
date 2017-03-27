#!/usr/bin/env python
import socket
import subprocess
import sys
import netaddr
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

# Ask for input
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Make the Pool of workers
pool = ThreadPool(512)

# Print a nice banner with information on which host we are about to scan
print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)

# Check what time the scan started
t1 = datetime.now()



# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

def pscan(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        sock.close()
        return

results = pool.map(pscan,range(1,1025))


#excepts

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print ('Scanning Completed in: ', total)
