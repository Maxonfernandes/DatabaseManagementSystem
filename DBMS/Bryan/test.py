
import mysql.connector as c

def display_men():
    db_config = {
    "host": "localhost",
    "user": "bryan",
    "password": "Bryan@123",
    "database": "OnlineShopping"
    }
    connection = c.connect(**db_config)
    cursor = connection.cursor()    
    query = " select * from Products where Category = 'Formals For Men' ;"
    cursor.execute(query)
    
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    print(result[0][2])
    out = ""
    for i in range(0,len(result)):
        out = out +" " + result[i][0] +" " + result[i][1] + " " + result[i][2] + ' ' + str(result[i][4])
        
    print(out)    
display_men()