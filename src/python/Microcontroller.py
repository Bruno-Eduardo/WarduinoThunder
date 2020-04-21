class Board():
    def __init__(self, name):
        self.name = name

class ArduinoUNO(Board):
    def __init__(self):
        super().__init__("Arduino UNO")
        self.num_of_digital_ports = 13
        self.num_of_analog_ports = 6
