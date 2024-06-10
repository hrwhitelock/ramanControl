from picam import *
import matplotlib.pyplot as plt
import numpy as np
import time
from python_to_labview import *

# initialize CCD
print "initializing..."
initializeCamera()

# get camera temperature
print "getting camera temp..."
temp = getCameraTemperature()
print "Camera temperature is %f C" % temp

# this will cool down CCD
print "setting camera temp..."
setCameraTemperature(-120)

# set binning
print "setting binning..."
setROI(1,1340,1,1,100,100)

# send config
print "sending configuration..."
sendConfiguration()
