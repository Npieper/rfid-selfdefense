import mysql.connector
from mysql.connector import Error
import datetime
from datetime import datetime, timedelta
from mail_service import send_alert_mail

def calculate_week_start_date():
    today = datetime.now().date()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)
    print("Today: " + str(today))
    print("Start: " + str(start))
    return start

def is_user_allowed(package_number, number_of_trainings):
    if package_number == 2:
        print("Package number is 2")
        if number_of_trainings > 3:
            print("WARNING: Client is not allowed to train that often!")
            send_alert_mail()
    elif package_number == 1:
        print("Package number is 1")
    elif package_number == 0:
        print("Package number is 0")

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

        week_start_day = calculate_week_start_date()

        cursor.execute("SELECT checkIn FROM time where checkIn > '{}'".format(week_start_day))

        count_rows = 0        
        for x in cursor:
            print(x.checkIn)
            count_rows += 1

        print(count_rows) 

        cursor.execute("SELECT package FROM user where ChipId = '{}'".format(1))
        
        package_number = -1
        for y in cursor:
            package_number = y.package
            
        is_user_allowed(package_number, count_rows)
           
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