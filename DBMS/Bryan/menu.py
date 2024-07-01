import tkinter as tk
from tkinter import PhotoImage
from pro import prod

def menu_main():
    menu = tk.Tk()
    menu.geometry("1000x1000") 
    menu.title("Online Shopping")
    label_select = tk.Label(menu, text="Select the option")
    label_select.place(x=400, y=50)  

    btn_pro = tk.Button(menu, text="Products",command=prod)
    btn_pro.place(x=430, y=100)  



    btn_cart = tk.Button(menu, text="Cart")
    btn_cart.place(x=460, y=200) 

    btn_order_summary = tk.Button(menu, text="Order Summary")
    btn_order_summary.place(x=380, y=300) 

        # Modifying the position of the label using place_configure()
        #label.place_configure(x=100, y=150)

    menu.mainloop()

#menu_main()