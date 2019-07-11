import sqlite3
import time
import datetime

def determine_training_session(day_as_number):
        training_session = None
        if day_as_number == 0:
                training_session = "Monday"         
        elif day_as_number == 1:
                training_session = "Tuesday"         
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

conn = sqlite3.connect('timetracking.db')

c = conn.cursor()


id = 2
name = 'derTest'
weekday_as_number = datetime.datetime.now().weekday()
the_date = datetime.datetime.now()  
training_session = determine_training_session(weekday_as_number)
                

c.execute("INSERT INTO user VALUES('{}', '{}', '{}')".format(id, name, the_date))
conn.commit()
conn.close()
                