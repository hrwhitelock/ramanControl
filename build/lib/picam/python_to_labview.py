"""
.. module: drivers/picam
   :platform: Windows
.. moduleauthor:: Daniel R. Dietze <daniel.dietze@berkeley.edu>

Basic interface to Princeton Instrument's PICam library. It supports most of the standard features
that are provided by PICam. I have decided not to implement a non-blocking version of the image
acquisition in order to keep things clear and simple.
rates on a PIXIS100::
"""

"""
These functions are for use by LabView applications
LabView doesn't allow access to python class objects, so
we create a camera object with the global name cam.
We then perform operations on that cam with the other functions.

written by Nick Pellatz (nickpellatz@gmail.com)
"""

from picam import *
import matplotlib.pyplot as plt
import numpy as np
import time

# initialize camera class and connect to library, look for available camera
# and connect to first one
def initializeCamera(dummy=0):
    global cam
    cam = picam()
    cam.loadLibrary()
    cam.connect()

##    cam.setParameter("ReadoutControlMode", PicamReadoutControlMode["FullFrame"])
##    cam.sendConfiguration()
    return

def getCameraTemperature():
    temp = cam.getParameter("SensorTemperatureReading")
    return temp

def setCameraTemperature(temp):
    cam.setParameter("SensorTemperatureSetPoint", temp)
    cam.sendConfiguration()
    return

def closeCamera(dummy=0):
    cam.disconnect()
    cam.unloadLibrary()
    return dummy

def setROI(xStart,xStop,xBin,yStart,yStop,yBin):
    cam.setROI(xStart-1,xStop-xStart+1,xBin,yStart-1,yStop-yStart+1,yBin)
    return

def setADC(quality,gain,speed):
    cam.setParameter("AdcSpeed", speed)
    cam.setParameter("AdcAnalogGain", gain)
    cam.setParameter("AdcQuality", quality)
    return

def setExposure(time):
    cam.setParameter("ExposureTime",time)
    return

def sendConfiguration():
    cam.sendConfiguration()
    return

def readOneFrame(exptime):
    dataList = cam.readNFrames(1,int(exptime+1000))
    data = dataList[0]
    data = data.reshape(1340)
    return data
    
def isRunning():
    return int(cam.isAcquisitionRunning())

def startAcquisition(dummy=0):
    cam.startAcquisition()
    return dummy

def stopAcquisition(dummy=0):
    cam.stopAcquisition()
    return dummy

def waitForFrame():
    exp = cam.getParameter("ExposureTime")
    
    w = cam.getRoiWidth()
    h = cam.getRoiHeight()
    
    dataList = cam.waitForFrame(exp)

    if dataList == []:
        return dataList
    
    data = dataList[0]
    
    data = data.reshape(h,w)
    extraRow = np.linspace(1,w,w)
    extraRow = extraRow.reshape(1,w)
    data = np.concatenate((data,extraRow), axis=0)
    return data
