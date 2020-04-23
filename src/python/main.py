#!/usr/bin/python3

import time

import SerialController
from Microcontroller import ArduinoUNO

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()
microcontroller = ArduinoUNO()

#TODO radio with headset button

def main():
    print(microcontroller.__dict__)


if __name__ == '__main__':
    main()
