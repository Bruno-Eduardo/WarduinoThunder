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
output = OutputController(keyboard, mouse)


def main():
    # main loop
    output_state = None
    while True:
        serial_input = serial.get_input()
        headset_input = headset.get_input()
        output.update(serial_input, headset_input)



if __name__ == '__main__':
    main()
