import mysql.connector as c
db_config = {
    "host": "localhost",
    "user": "bryan",
    "password": "Bryan@123",
    "database": "OnlineShopping"
}
connection = c.connect(**db_config)
cursor = connection.cursor()


query1 = "select * from Cart"  
for i in range(0,(int(input("Enter no. of input\n")))):
 Id = input("Enter Coustomer ID\n")
 P_Id = input("Enter Product ID\n")
 Pname = input("Enter Product name\n")
 Price = input("Enter price\n")
 Qty = input("Enter Quantity of the Item\n")
 query1 = f" insert into Cart values( '{Id}','{P_Id}','{Pname}','{Price}','{Qty}');" 
 cursor.execute(query1)
connection.commit()

query1 = "select * from Cart;"

cursor.execute(query1)



# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.commit()
connection.close()