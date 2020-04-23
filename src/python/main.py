#!/usr/bin/python3

import time

from SerialController import SerialController
from Microcontroller import ArduinoUNO

from HeadsetController import HeadsetController
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController



keyboard = KeyboardController()
mouse = MouseController()
headset = HeadsetController()

microcontroller = ArduinoUNO()
serial = SerialController(microcontroller)


def main():
    print(microcontroller.__dict__)


if __name__ == '__main__':
    main()
