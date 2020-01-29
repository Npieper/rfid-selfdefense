import mysql.connector
from mysql.connector import Error
import datetime
from datetime import datetime, timedelta

try:
    connection = mysql.connector.connect(
        host='rfid-selfdefense.chekdlwyhdsh.eu-central-1.rds.amazonaws.com',
        user='admin',
        database='rfid-selfdefense',
        port='3306',
        password=".,ejn-X(qTbh%$BE")

    if connection.is_connected():


        # Read in user with chip and save the chip id
        # ...

        cursor = connection.cursor(named_tuple=True)

        # Calculate start of the week
        today = datetime.now().date()
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        print("Today: " + str(today))
        print("Start: " + str(start))
        # ---------------------------

        cursor.execute("SELECT checkIn FROM time where checkIn > '{}'".format(start))

        countRows = 0        
        for x in cursor:
            print(x.checkIn)
            countRows += 1

        print(countRows) 

        cursor.execute("SELECT package FROM user where ChipId = '{}'".format(1))
        
        packageNumber = -1
        for y in cursor:
            packageNumber = y.package

        if packageNumber == 2:
            print("Package number is 2")
            if countRows > 3:
                print("WARNING: Client is not allowed to train that often!")
        elif packageNumber == 1:
            print("Package number is 1")
        elif packageNumber == 0:
            print("Package number is 0")
           
        # Have a look at the timezones, does not make sense right now    
        mySql_insert_query = "INSERT INTO time (userId, checkIn) VALUES ('{}', '{}')".format(1, datetime.now() + timedelta(hours=-1))
        result = cursor.execute(mySql_insert_query)
        connection.commit()
        print("Record inserted successfully into user table")
        cursor.close()


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")