import threading
import time

running_threads = []
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


class State():
    def __init__(self, first, serial_input, headset_input, keys=[]):
        self.first = first
        self.digital_input, self.analog_input = serial_input
        self.headset_input = headset_input

        [self.set_state_by_key(key) for key in keys]

        if len(self.analog_input) != 6: raise Exception('analog size was wrong')


    def set_state_by_key(self, key):
        if key in DIGITAL_PORT_MAPPER:
            self.__dict__.update({key.lower(): self.digital_input[DIGITAL_PORT_MAPPER[key.upper()]]})
        elif key in ANALOG_PORT_MAPPER:
            self.__dict__.update({key.lower(): self.analog_input[ANALOG_PORT_MAPPER[key.upper()]]})
        else:
            raise Exception('Key not found')


    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return 'State:' + str(self)


class OutputController():

    def __init__(self, keyboard, mouse):
        self.state = self.update(None)
        self.keyboard = keyboard
        self.mouse = mouse

    def update(self, new_input, headset_input=None):
        if new_input is None:
            print("Waiting for new inputs") # TODO change to logger
            self.state = None
            return

        first = self.state is None # TODO: check if this is really usefull

        self.old_state = self.state
        self.state = State( first,
                            new_input,
                            headset_input,
                            keys=[  'GEARS',
                                    'THROTTLE',])

        self.output_over_state_diff(self.state, self.old_state)

    def output_over_state_diff(self, state, old_state):
        if old_state is None:
            print('TODO old state is None') # TODO old state is None
            return

        if old_state.gears != state.gears:
            self.press_release(KEYBOARD_CONTROLL['TOGGLE_GEARS'])

    def set_gear(self, first):
        self.gears = self.digital_input[DIGITAL_PORT_MAPPER['GEARS']]


    def press_release(self, key, release_time=0.1):
        def assync_press():
            if key in running_threads: return
            running_threads.append(key)
            self.keyboard.press(key);
            time.sleep(release_time)
            self.keyboard.release(key)
            running_threads.remove(key)

        thr = threading.Thread(target=assync_press)
        thr.start()

def rising_edge(old, new):
    return (old == '0' and new == '1')
