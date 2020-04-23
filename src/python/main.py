#!/usr/bin/python3

import time

from SerialController import SerialController
from Microcontroller import ArduinoUNO
from OutputController import OutputController

from HeadsetController import HeadsetController
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController



keyboard = KeyboardController()
mouse = MouseController()
headset = HeadsetController()

microcontroller = ArduinoUNO()
serial = SerialController(microcontroller)
output = OutputController()


def main():
    # main loop
    output_state = None
    while True:
        new_input = serial.get_input()
        output_state = output.update(new_input)
        time.sleep(2)



if __name__ == '__main__':
    main()
