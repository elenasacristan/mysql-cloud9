import os
import datetime
import pymysql

#First we get our user name from Cloud9
#Thil will need to be modify if it is run in other environment

username = os.getenv('C9_USER')

#connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            


#try:
    #run query
    # with connection.cursor() as cursor:
    #     sql="Select * from Genre"
    #     cursor.execute(sql)
  #     # result = cursor.fetchall()
        # print(result)
       
       
#row by row in tuples        
#try:
    #run query
    # with connection.cursor() as cursor:
    #     sql="Select * from Genre"
    #     cursor.execute(sql)
        # result = cursor.fetchall()
        # print(result)
        
        # for row in cursor:
        #     print(row)        

#Display in dictionaries
#try:
    #run query
    # with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    #     sql="Select * from Genre"
    #     cursor.execute(sql)

    #     for row in cursor:
    #         print(row)        


#CREATING a TABLE
# try:
    #run query
    # with connection.cursor() as cursor:
    #   cursor.execute("""CREATE TABLE IF NOT EXISTS
    #                       Friends(name char(20), age int, DOB datetime);""")

#populate table Friends
# try:
#     #run query
#     with connection.cursor() as cursor:
#       cursor.execute("""Insert into Friends values("Pepe", 20, "1990-10-10 22:12:00")""")
#       connection.commit()


# try:
#     #run query
#     with connection.cursor() as cursor:
#       row = ("Bob", 30, "2000-8-8 12:12:12")
#       cursor.execute("Insert into Friends values (%s,%s,%s)", row)
#       connection.commit()



# Inserting many by using EXECUTEMANY
# try:
#     #run query
#     with connection.cursor() as cursor:
#       rows = [("Bob", 30, "2000-8-8 12:12:12"),
#             ("Juan", 12, "2003-8-8 10:12:12"),
#             ("Carlos", 100, "2002-8-8 11:12:12")]
#       cursor.executemany("Insert into Friends values (%s,%s,%s)", rows)
#       connection.commit()


# Update
# try:
#     #run query
#     with connection.cursor() as cursor:
#       name = (44, "Bob")
#       cursor.execute("Update Friends set age= %s where name= %s", name)
#       connection.commit()
      
# Update many
# try:
#     #run query
#     with connection.cursor() as cursor:
#       name = [(44, "Bob"),
#               (22, "Juan"),
#               (33, "Carlos")]
#       cursor.executemany("Update Friends set age= %s where name= %s", name)
#       connection.commit()

# Delete
# try:
#     #run query
#     with connection.cursor() as cursor:
#       name = "Bob"
#       cursor.execute("Delete from Friends where name= %s", name)
#       connection.commit()

# Delete Many
# try:
#     #run query
#     with connection.cursor() as cursor:
#       name = ["Bob","Pepe"]
#       cursor.executemany("Delete from Friends where name= %s", name)
#       connection.commit()

# Delete many without using executemany(exceutes n-times) but instead deleting all at once using DELETE WHERE IN
try:
    #run query
    with connection.cursor() as cursor:
      list_names = ["Juan","Carlos"]
      placeholder = ",".join(['%s']*len(list_names))
      cursor.execute("Delete from Friends where name in ({});".format(placeholder), list_names)
      connection.commit()

finally:
    #close connection regardless of whether the above was succesfull
    connection.close()
        