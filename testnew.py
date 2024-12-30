import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cafevia"
    )

# Fetch all products from the product table
def fetch_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    conn.close()
    return products

# Add product to cart table
def add_to_cart(proid):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cart (proid) VALUES (%s)", (proid,))
    conn.commit()
    conn.close()

# Fetch cart items
def fetch_cart():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cart")
    cart_items = cursor.fetchall()
    conn.close()
    return cart_items

# Update the sidebar cart section
def update_cart_sidebar():
    cart_items = fetch_cart()
    cart_list.delete(0, tk.END)
    for item in cart_items:
        cart_list.insert(tk.END, f"Product ID: {item[0]}")  # Adjust this line to show relevant data

# Add to cart button handler
def on_add_to_cart(proid):
    add_to_cart(proid)
    update_cart_sidebar()
    messagebox.showinfo("Success", "Product added to cart!")

# Create product card
def create_product_card(master, product):
    frame = tk.Frame(master)
    frame.pack(padx=10, pady=10)
    product_name = tk.Label(frame, text=product[1], font=("Arial", 14))
    product_name.pack()
    
    product_price = tk.Label(frame, text=f"Price: ${product[2]}", font=("Arial", 12))
    product_price.pack()
    
    add_button = tk.Button(frame, text="Add to Cart", command=lambda: on_add_to_cart(product[0]))
    add_button.pack()

# Tkinter setup
root = tk.Tk()
root.title("Cafevia")

# Sidebar for Cart
sidebar = tk.Frame(root, width=200, bg="lightgray", height=500)
sidebar.pack(side=tk.RIGHT, fill=tk.Y)

cart_label = tk.Label(sidebar, text="Your Cart", font=("Arial", 16), bg="lightgray")
cart_label.pack(pady=10)

cart_list = tk.Listbox(sidebar, width=30, height=15)
cart_list.pack(padx=10, pady=10)

# Main Content
content_frame = tk.Frame(root)
content_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Fetch and display products
products = fetch_products()
for product in products:
    create_product_card(content_frame, product)

# Start the Tkinter loop
root.mainloop()
