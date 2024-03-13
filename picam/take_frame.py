from picam import *
import matplotlib.pyplot as plt
import numpy as np
import time
from python_to_labview import *

# set exposure time
print "setting exposure time..."
setExposure(1)

startAcquisition()
    #time.sleep(1)
print "waiting..."
data = waitForFrame()
time.sleep(0.1)
print data
plt.figure()
plt.plot(data[0])
plt.show()
