"""
.. module: drivers/picam
   :platform: Windows
.. moduleauthor:: Daniel R. Dietze <daniel.dietze@berkeley.edu>

Basic interface to Princeton Instrument's PICam library. It supports most of the standard features
that are provided by PICam. I have decided not to implement a non-blocking version of the image
acquisition in order to keep things clear and simple.

Here is some example code showing the necessary parameters to get 1 kHz readout rates on a PIXIS100::
"""

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

# set exposure time
print "setting exposure time..."
setExposure(1)

# send config
print "sending configuration..."
sendConfiguration()

# run a for loop:
##for x in range(0,1):
##    print "starting..."
##    print "iteration: %f" % int(x+1)
##    startAcquisition()
##    #time.sleep(1)
##    print "waiting..."
##    data = waitForFrame()
##    time.sleep(0.1)
##    print data
startAcquisition()
    #time.sleep(1)
print "waiting..."
data = waitForFrame()
time.sleep(0.1)
print data
plt.figure()
plt.plot(data[0])
plt.show()

### start an acquisition
##print "starting acquisition..."
##startAcquisition()

### wait for a little bit
##print "waiting just to wait..."
##time.sleep(5)
##
### wait for the frame
##print "waiting for frame..."
##data = waitForFrame()
##
### print the result
##print "result of wait for frame:"
##print data

# close camera
print "closing camera..."
closeCamera()
print "goodbye"

### acquire a frame and print it
##plt.ion()
##fig = plt.figure()
##ax = fig.add_subplot(111)
##
##dataList = cam.readNFrames(1,exp*1000+1000)
##data = dataList[0]
##data = data.reshape(1340)
##
##pixels = np.linspace(1,1340,1340)
##line1, = ax.plot(pixels,data,'b-')
##plt.ylabel("Counts")
##plt.xlabel("Pixel")
##plt.axis([0,1340,500,7000])
##
##
##for i in np.linspace(1,100,100):
##    dataList = cam.readNFrames(1,exp*1000+1000)
##    data = dataList[0]
##    data = data.reshape(1340)
##
##    ##plt.figure()
##    ##plt.imshow(data,vmin=600,vmax=700)
##    ##plt.show()
##
##    line1.set_ydata(data)
##    fig.canvas.draw()


##cam.disconnect()
##cam.unloadLibrary()

