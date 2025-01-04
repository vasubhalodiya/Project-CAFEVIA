from tkinter import *
from tkinter import ttk
import MySQLdb

# Example window setup
AddCoffeeWindow = Tk()
AddCoffeeWindow.title("Add Product")

# Label for Product Category
lblProductCategory = Label(AddCoffeeWindow, text="Product Category", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
lblProductCategory.place(relx=0.07, rely=0.23)

# Dropdown (Combobox) for Product Category
categories = ["All", "Coffee", "Soft Drink", "Pizza", "Burger", "Dessert", "Food Meal"]
txtProductCategory = ttk.Combobox(AddCoffeeWindow, values=categories, font=("century gothic", 13), state="readonly")
txtProductCategory.place(relx=0.07, rely=0.28, relwidth=0.25, relheight=0.05)
txtProductCategory.set("All")  # Default selection

# Function to insert product with selected category into the database
def insert_product():
    product_category = txtProductCategory.get()
    
    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()
        
        # Insert data into the product table (example with other fields like name, price)
        product_name = "Sample Product"  # Replace with actual product name
        product_price = 100  # Replace with actual price
        
        cursor.execute("INSERT INTO product (procategory, proname, proprice) VALUES (%s, %s, %s)", 
                       (product_category, product_name, product_price))
        
        con.commit()
        print(f"Product added with category {product_category}")

    except Exception as e:
        print("Error while inserting product:", e)
    finally:
        if con:
            con.close()

# Example button to insert the product into the database
insert_button = Button(AddCoffeeWindow, text="Insert Product", command=insert_product, font=("century gothic bold", 13))
insert_button.place(relx=0.07, rely=0.35, relwidth=0.25, relheight=0.05)

AddCoffeeWindow.mainloop()
