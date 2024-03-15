import pylablib as pll
pll.par["devices/dlls/picam"] = "path/to/dlls"
from pylablib.devices import PrincetonInstruments

PrincetonInstruments.list_cameras()
cam = PrincetonInstruments.PicamCamera()

cam.set_attribute_value("Exposure Time", 0.1)
cam.get_attribute_value('Sensor Temperature Reading')

img = cam.snap()

signal = []
pixel = range(len(img[0]))
for i in range(len(img[0])):
    signal.append(sum(img[:, 1]))

plt.plot(pixel, signal)

with PrincetonInstruments.PicamCamera() as cam: # to close the camera automatically
    cam.start_acquisition()  # start acquisition (automatically sets it up as well)
    while True:  # acquisition loop
        cam.wait_for_frame()  # wait for the next available frame
        frame=cam.read_oldest_image()  # get the oldest image which hasn't been read yet
        # ... process frame ...