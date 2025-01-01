import MySQLdb
from tkinter import *
from tkinter import Toplevel
from PIL import Image, ImageTk

# Colors
sidecart_color, primary_color, secondary_color = "#F8F8F8", "#FF5733", "#FFFFFF"

# Database Helpers
def fetch_cart_data():
    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM cart")
            return cursor.fetchall()
    except Exception as e:
        print("Error fetching cart data:", e)
        return []

def update_cart(name, qty, price, label):
    qty = max(1, min(10, qty))
    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        with con.cursor() as cursor:
            cursor.execute("UPDATE cart SET cartqty = %s WHERE cartname = %s", (qty, name))
        label.config(text=str(qty))
    except Exception as e:
        print("Error updating cart:", e)

def populate_cart(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    for idx, (_, name, price, qty) in enumerate(fetch_cart_data()):
        card = Frame(frame, bg=sidecart_color)
        card.place(relx=0.05, rely=0.03 + idx * 0.18, relwidth=0.91, relheight=0.15)

        img = ImageTk.PhotoImage(Image.open('images/coffee.png').resize((50, 50)))
        Label(card, image=img, bg=sidecart_color).place(relx=0, rely=0, width=75, height=75)
        card.image = img  # Prevent garbage collection

        Label(card, text=name, bg=sidecart_color, fg=primary_color, font=("century gothic", 11)).place(relx=0.3, rely=0.15)
        Label(card, text=f"₹ {price}", bg=sidecart_color, font=("century gothic", 11)).place(relx=0.32, rely=0.55, relwidth=0.21)
        label_qty = Label(card, text=qty, bg=sidecart_color, font=("century gothic", 15))
        label_qty.place(relx=0.7, rely=0.55, width=22)

        Button(card, text="-", command=lambda n=name, q=int(qty): update_cart(n, q - 1, float(price), label_qty)).place(relx=0.6, rely=0.55, width=22)
        Button(card, text="+", command=lambda n=name, q=int(qty): update_cart(n, q + 1, float(price), label_qty)).place(relx=0.8, rely=0.55, width=22)

def update_total(label):
    cart_items = fetch_cart_data()
    total = sum(float(price) * int(qty) for _, _, price, qty in cart_items)
    label.config(text=f"₹ {total - (total * 0.20 if total > 800 else 0):.0f}")

# Order Functions
def place_order(name):
    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        with con.cursor() as cursor:
            cart_items = fetch_cart_data()
            if not cart_items:
                print("Cart is empty.")
                return
            for _, item, price, qty in cart_items:
                cursor.execute("INSERT INTO orders (ordername, orderqty, orderprice, customername) VALUES (%s, %s, %s, %s)", (item, qty, price, name))
            cursor.execute("DELETE FROM cart")
        populate_cart(cart_item_frame)
        update_total(total_label)
    except Exception as e:
        print("Error placing order:", e)

def open_customer_frame():
    customer_window = Toplevel(root)
    customer_window.geometry("300x150")
    Label(customer_window, text="Enter Customer Name:").pack(pady=10)
    name_var = StringVar()
    Entry(customer_window, textvariable=name_var).pack(pady=5)
    Button(customer_window, text="Submit", command=lambda: [place_order(name_var.get()), customer_window.destroy()]).pack(pady=10)

# GUI Setup
root = Tk()
root.geometry("800x600")

cart_frame = Frame(root, bg=sidecart_color)
cart_frame.place(relx=0.76, rely=0, relwidth=0.24, relheight=1)

cart_item_frame = Frame(cart_frame, bg=sidecart_color)
cart_item_frame.place(relx=0.05, rely=0.15, relwidth=0.91, relheight=0.6)

total_label = Label(cart_frame, text="₹ 0", bg=sidecart_color, font=("century gothic bold", 12))
total_label.place(relx=0.7, rely=0.77, relwidth=0.25)

Button(cart_frame, text="Place Order", command=open_customer_frame).place(relx=0, rely=0.86, relwidth=1)

populate_cart(cart_item_frame)
update_total(total_label)
root.mainloop()
