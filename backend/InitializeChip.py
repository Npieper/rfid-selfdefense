import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='us-cdbr-iron-east-02.cleardb.net',
                                         database='heroku_f88e5c34407b619',
                                         user='b525fb3beb7abe',
                                         password='431db98c')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()


        id = input("ID:")

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
