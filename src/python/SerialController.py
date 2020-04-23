import serial  # pyserial
import serial.tools.list_ports

import time

class SerialController():
    def __init__(self, microcontroller, timeout=2, sleep_after_init=2):
        self.microcontroller = microcontroller
        self.bytes_to_read = microcontroller.calc_bytes_to_read()
        self.baudrate = microcontroller.baudrate
        self.timeout = timeout
        self.sleep_after_init = sleep_after_init
        self.serial = self.connect(self.baudrate, self.timeout, self.sleep_after_init)

    def __del__(self):
        self.close_connection()

    def connect(self,baudrate, timeout, sleep_after_init):
        try:
            ser = serial.Serial('/dev/ttyACM0', baudrate, timeout=timeout)  # open serial port
            time.sleep(sleep_after_init)
            return ser
        except:
            print("No port ttyACM0") # TODO change to logger
            return None

    def close_connection(self):

        try:
            self.serial.close()
        except: # TODO which Exceptions?
            pass

    def read(self, bytes_to_read):
        read_bytes = []
        #for _ in range(bytes_to_read):
            #read_bytes.append(self.serial.read()) #TODO uncomment when arduino is working
            # b'W' = 01010111
            # read_bytes.append(b'W')
        read_bytes = [b'W',b'W',b'1',b'0',b'2',b'3',b',',b'1',b'0',b'2',b'3',b',',b'0',b'5',b'1',b'2',b',',b'0',b'5',b'1',b'2',b',',b'1',b'0',b'2',b'3',b',',b'1',b'0',b'2',b'3',b',']
        return read_bytes

    def update_input(self):
        self.raw_input = self.read(self.bytes_to_read)
        self.raw_digital, self.raw_analog = self.split_raw_input(self.raw_input)
        self.parsed_digital = self.parse_digital(self.raw_digital)
        self.parsed_analog = self.parse_analog(self.raw_analog)
        self.input = self.parsed_digital, self.parsed_analog

    def get_input(self):
        self.update_input()
        return self.input

    def byte_to_bit_list(self, byte_, byteorder="big"):
        int_from_byte = int.from_bytes(byte_, byteorder)
        single_string = bin(int_from_byte).split('b')[-1]
        single_string_zero_padding = ''.join(('00000000',single_string))[-8:]
        return single_string_zero_padding

    def split_raw_input(self, raw_input):
        bits_list = [self.byte_to_bit_list(byte_) for byte_ in raw_input]
        return bits_list[0:self.microcontroller.digital_bytes], \
                bits_list[self.microcontroller.digital_bytes: \
                            self.microcontroller.digital_bytes +
                            self.microcontroller.analog_bytes]

    def parse_digital(self, raw_digital):
        all_digital_bits = ''.join(raw_digital)[0:self.microcontroller.num_of_digital_ports]
        return all_digital_bits

    def parse_analog(self, raw_analog):
        chars_list = [chr(int(char, 2)) for char in raw_analog]
        splited_strings = ''.join(chars_list).split(',')
        splited_values = [int(string)for string in splited_strings  if string.isdigit() ]
        return splited_values
