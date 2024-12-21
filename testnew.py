import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Global variable to hold cart frame
cart_frame = None

# Database connection
def get_products():
    conn = mysql.connector.connect(
        host="localhost",  # Replace with your database host
        user="root",       # Replace with your database username
        password="",       # Replace with your database password
        database="product_cart"  # New database name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products LIMIT 5")  # Fetch 5 products
    products = cursor.fetchall()
    conn.close()
    return products

# Function to update cart and total price
class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.total = 0.0

    def add_to_cart(self, product):
        self.cart.append(product)
        self.total += product[2]  # Add product price to total
        update_cart_display(self.cart, self.total)

    def delete_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
            self.total -= product[2]  # Subtract product price from total
            update_cart_display(self.cart, self.total)

    def get_cart(self):
        return self.cart, self.total

# Function to update cart display
def update_cart_display(cart, total):
    global cart_frame
    if cart_frame:
        cart_frame.destroy()  # Clear current cart display
    create_cart_display(cart, total)

# Function to create a cart display
def create_cart_display(cart, total):
    global cart_frame
    cart_frame = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
    cart_frame.grid(row=0, column=3, padx=10, pady=10, rowspan=5, sticky="n")

    cart_text = "Cart:\n"
    for i, product in enumerate(cart):
        product_label = tk.Label(cart_frame, text=f"{product[1]} - ${product[2]:.2f}", font=("Arial", 12))
        product_label.grid(row=i, column=0, sticky="w")

        delete_button = tk.Button(cart_frame, text="Delete", command=lambda p=product: delete_from_cart(p))
        delete_button.grid(row=i, column=1)

    total_label = tk.Label(cart_frame, text=f"\nTotal: ${total:.2f}", font=("Arial", 14))
    total_label.grid(row=len(cart), column=0, columnspan=2)

# Function to delete item from the cart
def delete_from_cart(product):
    shopping_cart.delete_from_cart(product)

# Function to handle Add to Cart button click
def add_to_cart(product):
    shopping_cart.add_to_cart(product)

# Function to create product cards
def create_product_cards():
    products = get_products()
    row, col = 0, 0

    for product in products:
        frame = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
        frame.grid(row=row, column=col, padx=10, pady=10)

        name_label = tk.Label(frame, text=product[1], font=("Arial", 14))
        name_label.grid(row=0, column=0)

        price_label = tk.Label(frame, text=f"${product[2]:.2f}", font=("Arial", 12))
        price_label.grid(row=1, column=0)

        add_button = tk.Button(frame, text="Add to Cart", command=lambda p=product: add_to_cart(p))
        add_button.grid(row=2, column=0)

        col += 1
        if col == 3:
            col = 0
            row += 1

# Tkinter Setup
root = tk.Tk()
root.title("Product Shop")
root.geometry("800x600")

shopping_cart = ShoppingCart()

# Create product cards
create_product_cards()

# Start Tkinter loop
root.mainloop()
