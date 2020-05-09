class OutputController():
    LANDED = 0

    DIGITAL_PORT_MAPPER = { 'GEARS': 2,
                            'LEFT_PEDAL': 3,
                            'RIGHT_PEDAL': 4,
                            'FLAPS': 5,
                            'BRAKE': 6,
                            'AIR_BRAKE': 7,
                            'BOMB': 8,
                            'ROCKET': 9,
                            'JUMP':10,
                            'RELOAD':11,
                            'INIT_GROUND_OR_AIR':12,
                            'DIG_MISC1':13}
    ANALOG_PORT_MAPPER = {  'THROTTLE': 0,
                            'ELEVATOR': 1,
                            'AILERONS': 2,
                            'RUDDER': 3,
                            'ANALOG_MISC1': 4,
                            'ANALOG_MISC2': 5}
    KEYBOARD_CONTROLL = {'TOGGLE_GEARS': 'g'}

    def __init__(self):
        self.state = self.update(None)

    def update(self, new_input, headset_input=None):
        if new_input is None:
            print("Waiting for new inputs") # TODO change to logger
            self.state = None
            return self.state
        elif self.state is None and new_input is not None:
            first = True # TODO: check if this is really usefull
        else:
            first = False
            print("Just a normal update")

        self.old_state = self.state
        self.set_gear(first)
        self.set_throttle(first)

        self.state = (self.gears,
                      self.throttle)

        self.output_over_state_diff(state, old_state):
            if old_state is not None:
                if old_state.gears == LANDED and state.gears != LANDED:
                    self.press_release(KEYBOARD_CONTROLL['TOGGLE_GEARS']) # ASYNC HERE
            else:
                # TODO
                pass

    def set_gear(self, first):
        self.gears = self.digital_input[DIGITAL_PORT_MAPPER['GEARS']]


    def set_throttle(self, first):
        self.throttle = self.analog_input[ANALOG_PORT_MAPPER['THROTTLE']]
