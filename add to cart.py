import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",  # Change to your MySQL server host
    user="root",       # Change to your MySQL username
    password="",  # Change to your MySQL password
    database="store"  # Updated database name
)

cursor = db.cursor()

# Function to fetch products from database
def fetch_products():
    cursor.execute("SELECT * FROM items")  # Changed table name to items
    products = cursor.fetchall()
    return products

# Function to add product to cart
def add_to_cart(item_id, quantity):
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))  # Changed table name to items
    product = cursor.fetchone()
    
    if product:
        cursor.execute("INSERT INTO user_cart (item_id, quantity) VALUES (%s, %s)", (item_id, quantity))  # Changed table name to user_cart
        db.commit()
        messagebox.showinfo("Success", "Product added to cart!")
        refresh_cart()

# Function to fetch and display cart data
def refresh_cart():
    cursor.execute("SELECT c.id, i.name, c.quantity, i.price FROM user_cart c JOIN items i ON c.item_id = i.id")  # Changed table names to user_cart and items
    cart_items = cursor.fetchall()

    for widget in cart_frame.winfo_children():
        widget.destroy()  # Clear existing cart items

    total = 0
    for item in cart_items:
        # Create a frame to act as the "product card"
        card_frame = tk.Frame(cart_frame, relief="solid", borderwidth=1, padx=10, pady=10, width=250)
        card_frame.pack(fill="x", pady=5)

        # Product Name
        name_label = tk.Label(card_frame, text=item[1], font=("Helvetica", 14, "bold"))
        name_label.pack(anchor="w")

        # Price
        price_label = tk.Label(card_frame, text=f"Price: ${item[3]:.2f}", font=("Helvetica", 12))
        price_label.pack(anchor="w")

        # Quantity and total for this product
        quantity_label = tk.Label(card_frame, text=f"Quantity: {item[2]}", font=("Helvetica", 12))
        quantity_label.pack(anchor="w")

        total_price = item[3] * item[2]
        total_label_item = tk.Label(card_frame, text=f"Total: ${total_price:.2f}", font=("Helvetica", 12, "bold"))
        total_label_item.pack(anchor="w")

        total += total_price

    total_label.config(text=f"Total: ${total:.2f}")

# Function to place an order
def place_order():
    # Fetch all cart items
    cursor.execute("SELECT c.id, i.name, c.quantity, i.price FROM user_cart c JOIN items i ON c.item_id = i.id")
    cart_items = cursor.fetchall()

    # If cart is empty, show an error
    if not cart_items:
        messagebox.showerror("Error", "Your cart is empty!")
        return

    # Calculate total
    total = sum(item[3] * item[2] for item in cart_items)

    # Insert order into the orders table
    cursor.execute("INSERT INTO orders (total) VALUES (%s)", (total,))
    db.commit()
    order_id = cursor.lastrowid  # Get the last inserted order's ID

    # Insert order items into order_items table
    for item in cart_items:
        cursor.execute("INSERT INTO order_items (order_id, item_id, quantity, price) VALUES (%s, %s, %s, %s)",
                       (order_id, item[0], item[2], item[3]))
    db.commit()

    # Clear the cart
    cursor.execute("DELETE FROM user_cart")
    db.commit()

    messagebox.showinfo("Success", "Your order has been placed successfully!")
    refresh_cart()  # Refresh the cart section (it will be empty now)

# Create the main window
root = tk.Tk()
root.title("Store - Shopping Cart")

# Display products
products_frame = tk.Frame(root)
products_frame.pack(pady=10)

products = fetch_products()
for product in products:
    product_frame = tk.Frame(products_frame)
    product_frame.pack(fill='x', pady=5)

    product_label = tk.Label(product_frame, text=f"{product[1]} - ${product[2]:.2f}", font=("Helvetica", 12))
    product_label.pack(side='left')

    add_button = tk.Button(product_frame, text="Add to Cart", font=("Helvetica", 10), 
                           command=lambda pid=product[0]: add_to_cart(pid, 1))
    add_button.pack(side='right')

# Cart display with product card design
cart_frame = tk.Frame(root)
cart_frame.pack(pady=20)

cart_label = tk.Label(cart_frame, text="Your Cart:", font=("Helvetica", 16, "bold"))
cart_label.pack()

# Total Label at the bottom of cart
total_label = tk.Label(root, text="Total: $0.00", font=("Helvetica", 14, "bold"))
total_label.pack(pady=10)

# Place Order button
place_order_button = tk.Button(root, text="Place Order", font=("Helvetica", 14, "bold"), bg="green", fg="white", command=place_order)
place_order_button.pack(pady=20)

# Refresh cart display initially
refresh_cart()

# Run the Tkinter main loop
root.mainloop()

# Close the database connection
db.close()
