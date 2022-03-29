import pycom
import time



def deployTest():
    pycom.heartbeat(False)
    #colors in hexadecimal (0xRRGGBB)
    pycom.rgbled(0x00FF00)  # Green

