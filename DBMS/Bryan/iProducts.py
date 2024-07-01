import mysql.connector as c
db_config = {
    "host": "localhost",
    "user": "bryan",
    "password": "Bryan@123",
    "database": "OnlineShopping"
}
connection = c.connect(**db_config)
cursor = connection.cursor()


query = "select * from Products"  
for i in range(0,(int(input("Enter no. of input\n")))):
 P_Id = input("Enter Product ID\n")
 Pname = input("Enter Product name\n")
 Description = input("Enter Description\n")
 Category = input("Enter Type of Category\n")
 Price = input("enter price\n")
 query = f" insert into Products values( '{P_Id}','{Pname}','{Description}','{Category}','{Price}');" 
 cursor.execute(query)
connection.commit()

query = "select * from Products"

cursor.execute(query)



# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.commit()
connection.close()