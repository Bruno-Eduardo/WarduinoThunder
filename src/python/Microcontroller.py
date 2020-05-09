class Board():
    def __init__(self, name):
        self.name = name
        self.num_of_digital_ports = 0
        self.num_of_analog_ports = 0
        self.baudrate = 0

    def calc_bytes_to_read(self):
        self.digital_bytes = (self.num_of_digital_ports-8)//8+2
        self.analog_bytes = self.num_of_analog_ports * 4 + \
                            self.num_of_analog_ports         # b"0000," to b"1023,"
                                                        # for each analog pin
        return self.digital_bytes + self.analog_bytes

class ArduinoUNO(Board):
    def __init__(self):
        super().__init__("Arduino UNO")
        self.num_of_digital_ports = 13
        self.num_of_analog_ports = 6
        self.baudrate = 115200
        self.bytes_to_read = self.calc_bytes_to_read()
        print("Arduino bytes_to_read:", self.bytes_to_read)
