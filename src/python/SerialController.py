import serial  # pyserial
import serial.tools.list_ports

import time


def connect(baudrate, timeout=2, sleep_after_init=2):
    try:
        ser = serial.Serial('/dev/ttyACM0', baudrate, timeout=timeout)  # open serial port
        time.sleep(sleep_after_init)
        return ser
    except:
        print("No port ttyACM0")
        return None

def fechar(ser):
    ser.close()
