#!/usr/bin/env python

import sqlite3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, name = reader.read()
        print(id)
        print(name)


        conn = sqlite3.connect('timetracking.db')

        c = conn.cursor()

        c.execute("""CREATE TABLE user (
                 uuid integr,
                 name text
         ) """)

        c.execute(f"INSERT INTO user VALUES({id}, {name})")
        conn.commit()
        conn.close()
finally:
        GPIO.cleanup()

