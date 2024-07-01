import mysql.connector as c
db_config = {
    "host": "localhost",
    "user": "bryan",
    "password": "Bryan@123",
    "database": "OnlineShopping"
}
connection = c.connect(**db_config)
cursor = connection.cursor()


query1 = "select * from Payment"  
for i in range(0,(int(input("Enter no. of input\n")))):
 Pay_Id = input("Enter Payment ID\n")
 Id = input("Enter Coustomer ID\n")
 Amount = input("Total Amount\n")
 Pay_type = input("Enter Method of Payment\n")
 query1 = f" insert into Payment values( '{Pay_Id}','{Id}','{Amount}','{Pay_type}');" 
 cursor.execute(query1)
connection.commit()

query1 = "select * from Payment;"

cursor.execute(query1)



# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.commit()
connection.close()