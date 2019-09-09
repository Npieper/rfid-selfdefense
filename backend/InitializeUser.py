#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sqlite3


reader = SimpleMFRC522()

try:
        id = input('Bitte ID eingeben.')
        print("Jetzt den Chip auf das Lesegeraet legen.")
        reader.write(id)
        print("Chip beschrieben.")

        conn = sqlite3.connect('timetracking.db')
        c  = conn.cursor()

        c.execute("INSERT INTO user id VALUES('{}')".format(id))

        conn.commit()
        conn.close()


finally:
        GPIO.cleanup()
