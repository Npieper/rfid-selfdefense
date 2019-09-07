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
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")