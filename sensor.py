try:
    import RPi.GPIO as GPIO  # import RPi.GPIO module/pip install GPIOSimulator
except ModuleNotFoundError:
    from GPIOEmulator.EmulatorGUI import GPIO


class Pin:
    def __init__(self, pos: int, is_output: bool):
        self.pos = pos
        self.is_output = is_output
        self.setup_gpio()

    def setup_gpio(self):
        if self.is_output:
            GPIO.setup(self.pos, GPIO.OUT)
        else:
            GPIO.setup(self.pos, GPIO.IN)

    def toggle(self, val):
        GPIO.output(self.pos, val)


class Sensor:
    def __init__(self, pin: Pin, val_type: str):
        self.pin = pin
        self.val_type = val_type

    def get_value(self):
        if self.pin.is_output:
            return 0
        else:
            return GPIO.input(self.pin.pos)

    def toggle_sensor(self, toggle_on: bool):
        if self.pin.is_output:
            self.pin.toggle(toggle_on)
