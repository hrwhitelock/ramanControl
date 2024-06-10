import pylablib as pll
pll.par["devices/dlls/picam"] = "path/to/dlls"
from pylablib.devices import PrincetonInstruments
cam = PrincetonInstruments.PicamCamera()
print(PrincetonInstruments.list_cameras())
cam.close()
