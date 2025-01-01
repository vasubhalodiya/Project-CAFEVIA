import tkinter as tk
import mysql.connector

# Connect to MySQL Database
def fetch_products(category=None):
    conn = mysql.connector.connect(
        host='localhost',     # Database host
        user='root', # Your MySQL username
        password='', # Your MySQL password
        database='try'    # Your database name
    )
    cursor = conn.cursor()
    
    # Query to fetch products based on category
    if category:
        query = "SELECT name FROM product WHERE category = %s"
        cursor.execute(query, (category,))
    else:
        query = "SELECT name FROM product"
        cursor.execute(query)
    
    products = cursor.fetchall()  # Fetch all the rows
    conn.close()
    return [product[0] for product in products]  # Return a list of product names

# Function to update the display with product labels
def update_display(products):
    # Clear the current labels in the product_frame
    for widget in product_frame.winfo_children():
        widget.destroy()
    
    # Create and pack labels for each product
    for product in products:
        label = tk.Label(product_frame, text=product, relief="solid", width=20, height=2)
        label.pack(side=tk.LEFT, padx=5, pady=5)

# Button click functions to filter the products
def show_all():
    products = fetch_products()  # Get all products
    update_display(products)

def show_coffee():
    products = fetch_products("coffee")  # Get coffee products
    update_display(products)

def show_pizza():
    products = fetch_products("pizza")  # Get pizza products
    update_display(products)

# Create the main window
root = tk.Tk()
root.title("Product Filter")

# Create buttons for each category
button_all = tk.Button(root, text="All", command=show_all)
button_coffee = tk.Button(root, text="Coffee", command=show_coffee)
button_pizza = tk.Button(root, text="Pizza", command=show_pizza)

# Pack buttons
button_all.pack(pady=5)
button_coffee.pack(pady=5)
button_pizza.pack(pady=5)

# Frame to hold the product labels
product_frame = tk.Frame(root)
product_frame.pack(pady=20)

# Initialize the display with all products
show_all()

# Run the Tkinter main loop
root.mainloop()
