import os
import pymysql

#First we get our user name from Cloud9
#Thil will need to be modify if it is run in other environment

username = os.getenv('C9_USER')

#connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            


try:
    #run query
    with connection.cursor() as cursor:
        sql="Select * from Genre"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    #close connection regardless of whether the above was succesfull
    connection.close()
        