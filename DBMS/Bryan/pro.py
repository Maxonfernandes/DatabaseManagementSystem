import tkinter as tk
import mysql.connector as c

def prod():
    def display_men():
        db_config = {
        "host": "localhost",
        "user": "bryan",
        "password": "Bryan@123",
        "database": "OnlineShopping"
        }
        connection = c.connect(**db_config)
        cursor = connection.cursor()
        query = "select * from Products Where Category = 'Formals For Men';"
        cursor.execute(query)
    
        #connection.commit()
        rows = cursor.fetchall()

        for row_index, row_data in enumerate(rows):
            for col_index, cell_data in enumerate(row_data):
                table_label = tk.Label(pro, text=cell_data)
                table_label.grid(row=row_index, column=col_index)  
                #table_label.place(x=1000,y=400)
        connection.close()
        connection.commit()
        connection.close()
    def display_wmen():
        db_config = {
        "host": "localhost",
        "user": "bryan",
        "password": "Bryan@123",
        "database": "OnlineShopping"
        }
        connection = c.connect(**db_config)
        cursor = connection.cursor()    
        query = " select * from Products where Category = 'Ethnic For Women' ;"
        cursor.execute(query)
        
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        
        out = ""
        for i in range(0,len(result)):
            out = out +" " + result[i][0] +" " + result[i][1] + " " + result[i][2] + ' ' + str(result[i][4])
            out_label = tk.Label(pro, text= out)
            out_label.place(x=100,y=600) 
            
            
    def display_cwmen():
        db_config = {
        "host": "localhost",
        "user": "bryan",
        "password": "Bryan@123",
        "database": "OnlineShopping"
        }
        connection = c.connect(**db_config)
        cursor = connection.cursor()    
        query = " select * from Products where Category = 'Casuals Women' ;"
        cursor.execute(query)
        
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        
        out = ""
        for i in range(0,len(result)):
            out = out +" " + result[i][0] +"  " + result[i][1] + "  " + result[i][2] + '  ' + str(result[i][4])
            out_label = tk.Label(pro, text= out)
            out_label.place(x=100,y=600)
    def display_cmen():
        db_config = {
        "host": "localhost",
        "user": "bryan",
        "password": "Bryan@123",
        "database": "OnlineShopping"
        }
        connection = c.connect(**db_config)
        cursor = connection.cursor()    
        query = " select * from Products where Category = 'Casuals For Men' ;"
        cursor.execute(query)
        
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        
        out = ""
        for i in range(0,len(result)):
            out = out +" " + result[i][0] +" " + result[i][1] + " " + result[i][2] + "    " + str(result[i][4])
            out_label = tk.Label(pro, text= out)
            out_label.place(x=100,y=600)        
    


    pro = tk.Tk()
    pro.geometry("1250x1000")  # Set the dimensions of the window
    pro.title("Product Categories")
    label = tk.Label(pro, text="Categories")
    label.place(x=550, y=50)  # Initial placement of the label

    btn_for_men = tk.Button(pro, text="Formals for men", command = display_men)
    btn_for_men.place(x=50, y=100) 

    btn_eth_wmen = tk.Button(pro, text="Ethnic for women", command= display_wmen)
    btn_eth_wmen.place(x=330,y=100)

    btn_cas_men = tk.Button(pro, text="Casuals for men", command= display_cmen)
    btn_cas_men.place(x=620,y=100)

    btn_cas_wmen = tk.Button(pro, text="Casuals for women",command= display_cwmen)
    btn_cas_wmen.place(x=900,y=100)

    #label.place_configure(x=100, y=150)

    pro.mainloop()
#prod()