# Define the maximum quantity
MAX_QUANTITY = 10

# Database connection and functions
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

def update_cart(cart_name, new_qty, price, label_qty):
    if new_qty < 1:
        new_qty = 1
    if new_qty > 10:
        new_qty = 10

    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()
        cursor.execute("UPDATE cart SET cartqty = %s WHERE cartname = %s", (new_qty, cart_name))
        con.commit()
        label_qty.config(text=str(new_qty))  # Update the quantity label immediately
    except Exception as e:
        print("Error updating cart:", e)
    finally:
        if con:
            con.close()

def remove_from_cart(cart_name, card):
    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()
        cursor.execute("DELETE FROM cart WHERE cartname = %s", (cart_name,))
        con.commit()
        print(f"Removed {cart_name} from the cart")
        card.destroy()  # Remove the product card from the UI
    except Exception as e:
        print("Error removing from cart:", e)
    finally:
        if con:
            con.close()

def populate_cart(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    cart_items = fetch_cart_data()
    for idx, (cart_id, name, price, qty) in enumerate(cart_items):
        total = int(qty) * float(price)
        card = Frame(frame, background=sidecart_color)
        card.place(relx=0.05, rely=0.03 + (idx * 0.18), relwidth=0.91, relheight=0.15)

        img = Image.open('images/coffee.png').resize((50, 50))
        img = ImageTk.PhotoImage(img)
        Label(card, image=img, bg=sidecart_color).place(relx=0, rely=0, width=75, height=75)
        card.image = img  # Keep reference to avoid garbage collection

        Label(card, text=name, bg=sidecart_color, fg=primary_color, font=("century gothic bold", 11)).place(relx=0.3, rely=0.15)
        Label(card, text=f"₹ {price}", bg=price_color, fg=secondary_color, font=("century gothic bold", 11)).place(relx=0.32, rely=0.55, relwidth=0.21, height=22)
        label_qty = Label(card, text=qty, bg=sidecart_color, fg=primary_color, font=("century gothic bold", 15))
        label_qty.place(relx=0.7, rely=0.55, width=22, height=22)

        Button(card, text="-", font=("century gothic bold", 15), bg=primary_color, fg=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda n=name, q=int(qty), p=float(price), label_qty=label_qty: update_cart(n, q - 1, p, label_qty)).place(relx=0.6, rely=0.55, width=22, height=22)
        Button(card, text="+", font=("century gothic bold", 15), bg=primary_color, fg=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda n=name, q=int(qty), p=float(price), label_qty=label_qty: update_cart(n, q + 1, p, label_qty)).place(relx=0.8, rely=0.55, width=22, height=22)

        # Remove button to remove the item from the cart
        Button(card, text="Remove", font=("century gothic bold", 10), bg="red", fg=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda n=name, card=card: remove_from_cart(n, card)).place(relx=0.85, rely=0.02, width=60, height=20)

# Assuming you have a frame for cart items
populate_cart(cart_item_frame)
