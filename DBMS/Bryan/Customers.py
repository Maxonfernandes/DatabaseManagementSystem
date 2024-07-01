import mysql.connector as c
db_config = {
    "host": "localhost",
    "user": "bryan",
    "password": "Bryan@123",
    "database": "OnlineShopping"
}
connection = c.connect(**db_config)
cursor = connection.cursor()


query = "select * from Customer"  
for i in range(0,(int(input("Enter no. of input\n")))):
 P_Id = input("Enter Customer ID\n")
 Username = input("Enter  Username\n")
 Password = input("Enter Password\n")
 Fname = input("Enter Type First name\n")
 Lname = input("Enter Last name\n")
 Address = input("Enter Address\n")
 Phone = input("Enter Phone No\n")
 query = f" insert into Customer values( '{P_Id}','{Username}','{Password}','{Fname}','{Lname}','{Address}','{Phone}');" 
 cursor.execute(query)
connection.commit()

query = "select * from Customer"

cursor.execute(query)



# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.commit()
connection.close()