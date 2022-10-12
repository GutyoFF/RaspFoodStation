import unittest
import requests as http
try:
    import RPi.GPIO as GPIO  # import RPi.GPIO module/pip install GPIOSimulator
except ModuleNotFoundError:
    from GPIOEmulator.EmulatorGUI import GPIO


class RunTest(unittest.TestCase):
    def setUp(self) -> None:
        GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD

    def test_1(self):
        print('xd')

    def tearDown(self) -> None:
        GPIO.cleanup()


if __name__ == '__main__':
    unittest.main()
