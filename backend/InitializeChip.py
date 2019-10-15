import mysql.connector
from mysql.connector import Error
from mfrc522 import SimpleMFRC522

try:
    connection = mysql.connector.connect(host='us-cdbr-iron-east-02.cleardb.net',
                                         database='heroku_f88e5c34407b619',
                                         user='b525fb3beb7abe',
                                         password='431db98c')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        
        reader = SimpleMFRC522()

        id = input('Bitte ID eingeben.')
        print("Jetzt den Chip auf das Lesegeraet legen.")
        reader.write(id)
        print("Chip beschrieben.")


        mySql_insert_query = "INSERT INTO user (ChipID) VALUES ('{}')".format(id)
        cursor = connection.cursor()
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
