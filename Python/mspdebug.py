# mspdebug.py
import settings
import serial
import painting
from time import sleep
from threading import *

# Send bytes to msp
def send_to_msp( firstc, secondc ):
    painting.paint_gui( firstc, secondc )
    return
    ser = serial.Serial(settings.devserial)
    ser.write(bytes([firstc]))
    ser.write(bytes([secondc]))
    print(bytes([firstc]))
    print(bytes([secondc]))
    ser.close()

# Turn off semaphores
def turnoff_semaphores():
    send_to_msp(0,0);
