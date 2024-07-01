import mysql.connector as c
db_config = {
    "host": "localhost",
    "user": "bryan",
    "password": "Bryan@123",
    "database": "OnlineShopping"
}
connection = c.connect(**db_config)
cursor = connection.cursor()


query1 = "select * from Order_details"  
for i in range(0,(int(input("Enter no. of input\n")))):
 Order_id = input("Enter Order ID\n")
 P_Id = input("Enter Customer ID\n")
 Arriving = input("Enter Arraving Date\n")
 query1 = f" insert into Order_details values( '{Order_id}','{P_Id}','{Arriving}');" 
 cursor.execute(query1)
connection.commit()

query1 = "select * from Order_details;"
connection.commit()

cursor.execute(query1)



# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.commit()
connection.close()