import tkinter as tk
from tkinter import messagebox
import menu

import pro

#from Customers import * 
def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Bryan05" and password == "bry573":
        messagebox.showinfo("Login", "Login successful!")
        login.destroy()
        menu.menu_main()
        menu.destory()
        pro.prod()
        
        
        
    elif  username == "Maxi29" and password == "maxon1203":
        messagebox.showinfo("Login", "Login successful!")
        login.destroy()
        menu.menu_main()
        menu.destory()
        pro.prod()
        
    else:
        messagebox.showerror("Login", "Invalid credentials")
        
        

login = tk.Tk()
login.geometry("700x700")
login.title("Login Page")
# Create and place widgets
tk.Label(login, text="Username:").pack()
username_entry = tk.Entry(login)
username_entry.pack()

tk.Label(login, text="Password:").pack()
password_entry = tk.Entry(login, show="*")
password_entry.pack()

login_button = tk.Button(login, text="Login", command=authenticate)
login_button.pack()
new_user_btn = tk.Button(login, text = "New User" , command =authenticate)
new_user_btn.pack()
# Run the main event loop
login.mainloop()

