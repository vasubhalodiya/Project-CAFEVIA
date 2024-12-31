import MySQLdb
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *

# Function to fetch cart data from the database
def fetch_cart_data():
    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM cart")  # Fetch all cart items
        return cursor.fetchall()
    except Exception as e:
        print("Error fetching cart data:", e)
        return []
    finally:
        if con:
            con.close()

# Function to update item quantity in the cart
def update_cart(cart_name, new_qty, price):
    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()
        total = new_qty * price
        cursor.execute("UPDATE cart SET cartqty = %s, carttotal = %s WHERE cartname = %s", (new_qty, total, cart_name))
        con.commit()
    except Exception as e:
        print("Error updating cart:", e)
    finally:
        if con:
            con.close()

# Function to create cart cards dynamically
def populate_cart(frame):
    for widget in frame.winfo_children():  # Clear existing widgets
        widget.destroy()

    cart_items = fetch_cart_data()

    for idx, (cart_id, name, qty, price, total) in enumerate(cart_items):
        card = Frame(frame, bg="lightgray")
        card.place(relx=0.05, rely=0.16 + (idx * 0.12), relwidth=0.91, relheight=0.11)

        # Product image (placeholder)
        img = Image.open('images/coffee.png').resize((60, 60))
        img = ImageTk.PhotoImage(img)
        Label(card, image=img, bg="lightgray").place(relx=0, rely=0.09, width=75, height=75)
        card.image = img  # Keep reference to avoid garbage collection

        # Product details
        Label(card, text=name, bg="lightgray", fg="black", font=("Arial", 12)).place(relx=0.3, rely=0.1)
        Label(card, text=f"₹ {price}", bg="white", fg="black", font=("Arial", 12)).place(relx=0.32, rely=0.5, width=50)

        # Quantity controls
        Button(card, text="-", command=lambda n=name, q=qty, p=price: update_cart(n, max(1, q - 1), p), width=2).place(relx=0.6, rely=0.5)
        Label(card, text=qty, bg="lightgray", fg="black", font=("Arial", 12)).place(relx=0.7, rely=0.5, width=20)
        Button(card, text="+", command=lambda n=name, q=qty, p=price: update_cart(n, q + 1, p), width=2).place(relx=0.8, rely=0.5)

# Main window and frame
root = tk.Tk()
root.geometry("500x500")
MenuCartFrame = Frame(root, bg="white")
MenuCartFrame.pack(fill="both", expand=True)

populate_cart(MenuCartFrame)  # Load the cart

root.mainloop()
