import unittest
from json import JSONDecoder

import requests as http

from local.local_data_source import LocalDataSource
from sensor import *

try:
    import RPi.GPIO as GPIO  # import RPi.GPIO module/pip install GPIOSimulator
except ModuleNotFoundError:
    from GPIOEmulator.EmulatorGUI import GPIO


class RunTest(unittest.TestCase):
    def setUp(self) -> None:
        GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD

    def test_1(self):
        button = Sensor(Pin(19, False), bool, lambda b: print(b, 'x'))
        led = Sensor(Pin(13, True), bool, lambda b: print(b, 'l'))
        print(led.get_value())
        while True:
            while button.get_value():
                led.toggle_sensor(True)

            while not button.get_value():
                led.toggle_sensor(False)

    def test_2(self):
        res = http.get('https://genshin-app-api.herokuapp.com/api/characters/info/Amber/')
        response = JSONDecoder().decode(res.text)
        print(response['message'])

    def test_3(self):
        data = LocalDataSource()
        res = data.db_cursor.execute("CREATE TABLE test(col_1 int, col_2 varchar(10))")
        print(res)

    def tearDown(self) -> None:
        GPIO.cleanup()


if __name__ == '__main__':
    unittest.main()
