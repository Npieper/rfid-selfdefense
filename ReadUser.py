#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import datetime
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
conn = sqlite3.connect('timetracking.db')
c = conn.cursor()

def determine_training_session(day_as_number):
        training_session = None
        if day_as_number == 0:
                training_session = "Kickboxing"         
        elif day_as_number == 1:
                training_session = "KravMaga"         
        elif day_as_number == 2:
                training_session = "Wednesday"         
        elif day_as_number == 3:
                training_session = "Thursday"         
        elif day_as_number == 4:
                training_session = "Friday"         
        elif day_as_number == 5:
                training_session = "Saturday"         
        elif day_as_number == 6:
                training_session = "Sunday"   

        return training_session

while True:

        try:
                id, name = reader.read()
                print(id)
                print("User acknowledged!")

                weekday_as_number = datetime.datetime.now().weekday()
               
                training_session = determine_training_session(weekday_as_number)

                date = datetime.datetime.now()
                
                c.execute("INSERT INTO user VALUES('{}', '{}', '{}')".format(id, name, date, training_session))

                conn.commit()
                conn.close()
                
                time.sleep(3)
        finally:
                GPIO.cleanup()

