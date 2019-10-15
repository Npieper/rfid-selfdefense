#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

while True:

        try:
                id, uuid = reader.read()
                print(uuid)
                print("User acknowledged!")
                
                time.sleep(3)
        finally:
                GPIO.cleanup()

