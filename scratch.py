import pylablib as pll
pll.par["devices/dlls/picam"] = "path/to/dlls"
from pylablib.devices import PrincetonInstruments

import matplotlib.pyplot as plt
import numpy as np

PrincetonInstruments.list_cameras()
cam = PrincetonInstruments.PicamCamera()

cam.set_attribute_value("Exposure Time",1000*300)
cam.get_attribute_value('Sensor Temperature Reading')
# cam.set_attribute_value("ROIs", CPicamRoi(x=0,width=1340,x_binning0,100,1,100])
# cam.set_
fname = 'k3_4_real_actual_this_time_no_really.txt'
fpath = os.path.join(path, fname)
file = open(fpath, 'a')

img = cam.snap(timeout = 1e6)

signal = []
pixel = range(len(img[0]))
for i in range(len(img[0])):
    signal.append(sum(img[:, i]))

plt.plot(pixel, signal)
plt.show() 


nmArr = []
cmArr = []

for i in range(1340):
     nm = (-7/(1299-744)*(i-744)+597)
     nmArr.append(nm)
     cm = 10000000/532 -10000000/nm
     cmArr.append(cm)

for i in range(len(signal)):
    file.write(str(nmArr[i]) + ','+str(cmArr[i])+','+str(signal[i])+'\n')

with PrincetonInstruments.PicamCamera() as cam: # to close the camera automatically
    cam.start_acquisition()  # start acquisition (automatically sets it up as well)
    while True:  # acquisition loop
        cam.wait_for_frame()  # wait for the next available frame
        frame=cam.read_oldest_image()  # get the oldest image which hasn't been read yet
        # ... process frame ...



def takeSpectrum(start, stop): 
    #HARD CODED CONVERSION FOR NOW
    #FIX THIS DUMBASS
    '''
        start and stop input in nm bc my brain is tired and i keep fucking up the conversion. 
        output saves both nm and cm^-1 so its fine
    '''
    # assumes start and stop input in cm^-1 shift, since thats how we normallyt talk abotu it
    # start by converting start and stop to nm
    # nmStart = wavNumToNM(float(start))
    # nmStop = wavNumToNM(float(stop))

    #now we move the spec to the start 
    #note - this will overshoot! personally, i don't care
    #i'd rather take more data & am writing this so it just takes a fuckload of data
    #can be rewritten in future
# wavelenArr =[]
# wavNumArr = []
# signal = []
wavelen = []
raman = []
data = []
for pos in np.arange(float(start), float(stop), 1):
    # Mono1.approachWL(pos)
    # img = cam.snap()
    #now figure out what the axis was 
    #yikes
    #remember pos is the detector center, not edge
    #all of this is ahrd coded but should be switched with a calibration process to do at the start f the day
    px1 = 724 #center wavelength position
    px2 = 1285 # low edge (7nm below)
    deltaL = -7
    pixel = range(0,1340)

    for i in range(0,1340):
        wav = pos+ ((deltaL/(px2-px1))*(pixel[i]-px1))
        wavelen.append(wav)
        raman.append(1/laser - 1/(wav*10**(-7)))
        data.append(np.random.random())


    plt.plot(raman, data)