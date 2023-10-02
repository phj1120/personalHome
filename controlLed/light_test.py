from time import sleep
import RPi.GPIO as GPIO


#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

while True:
    print(GPIO.input(27))
    time.sleep(1)