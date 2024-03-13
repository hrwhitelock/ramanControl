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

# initialize camera class and connect to library, look for available camera and connect to first one
cam = picam()
cam.loadLibrary()
cam.getAvailableCameras()
cam.connect()

# this will cool down CCD
cam.setParameter("SensorTemperatureSetPoint", -120)

# shortest expoure
exp = 0
cam.setParameter("ExposureTime", exp*1000)

# readout mode
cam.setParameter("ReadoutControlMode", PicamReadoutControlMode["FullFrame"])

# custom chip settings
##cam.setROI(0, 1340, 1, 0, 100, 100)
cam.setParameter("ActiveWidth", 1340)
cam.setParameter("ActiveHeight", 100)
cam.setParameter("ActiveLeftMargin", 0)
cam.setParameter("ActiveRightMargin", 0)
cam.setParameter("ActiveTopMargin", 8)
cam.setParameter("ActiveBottomMargin", 8)
# cam.setParameter("VerticalShiftRate", 3.2)    # select fastest

# set logic out to not ready
# cam.setParameter("OutputSignal", PicamOutputSignal["Busy"])

# shutter delays; open before trigger corresponds to shutter opening pre delay
# cam.setParameter("ShutterTimingMode", PicamShutterTimingMode["Normal"])
# cam.setParameter("ShutterClosingDelay", 0)

### sensor cleaning
##cam.setParameter("CleanSectionFinalHeightCount", 1)
##cam.setParameter("CleanSectionFinalHeight", 100)
##cam.setParameter("CleanSerialRegister", False)
##cam.setParameter("CleanCycleCount", 1)
##cam.setParameter("CleanCycleHeight", 100)
##cam.setParameter("CleanUntilTrigger", True)

# sensor gain settings
# according to manual, Pixis supports 100kHz and 2MHz; select fastest
cam.setParameter("AdcSpeed", 2.0)
cam.setParameter("AdcAnalogGain", PicamAdcAnalogGain["High"])
cam.setParameter("AdcQuality", PicamAdcQuality["LowNoise"])

# trigger and timing settings
# cam.setParameter("TriggerDetermination", PicamTriggerDetermination["PositivePolarity"])
# cam.setParameter("TriggerResponse", PicamTriggerResponse["ReadoutPerTrigger"])

# send configuration
cam.sendConfiguration()

# get readout speed
print "Estimated readout time = %f ms" % cam.getParameter("ReadoutTimeCalculation")

print "Sensor temperature is %f C" % cam.getParameter("SensorTemperatureReading")

print "Set exposure time is %f ms" % cam.getParameter("ExposureTime")

# set the roi
cam.setROI(0,1340,1,0,100,100)
cam.sendConfiguration()

# acquire a frame and print it
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

dataList = cam.readNFrames(1,exp*1000+1000)
data = dataList[0]
data = data.reshape(1340)

pixels = np.linspace(1,1340,1340)
line1, = ax.plot(pixels,data,'b-')
plt.ylabel("Counts")
plt.xlabel("Pixel")
plt.axis([0,1340,500,7000])


for i in np.linspace(1,100,100):
    dataList = cam.readNFrames(1,exp*1000+1000)
    data = dataList[0]
    data = data.reshape(1340)

    ##plt.figure()
    ##plt.imshow(data,vmin=600,vmax=700)
    ##plt.show()

    line1.set_ydata(data)
    fig.canvas.draw()


cam.disconnect()
cam.unloadLibrary()

