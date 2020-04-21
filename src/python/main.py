import time

import SerialController
from Microcontroller import ArduinoUNO

# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

microcontroller = ArduinoUNO()

def main():
    print(microcontroller.__dict__)


if __name__ == '__main__':
    main()
