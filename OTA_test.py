import pycom
import time



def deployTest():
    pycom.heartbeat(False)
    #colors in hexadecimal (0xRRGGBB)
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(3)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(3)
    pycom.heartbeat(False)

