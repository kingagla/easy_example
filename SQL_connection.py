import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     database='sales',
                                     user='root',
                                     password='MyPassword')


print(connection.is_connected())