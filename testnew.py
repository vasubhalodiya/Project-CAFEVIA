# Function to insert cart data into the orders table
def place_order():
    try:
        # Fetch cart data from the database
        cart_items = fetch_cart_data()  # Fetch cart data (cart_id, name, qty, price)

        if not cart_items:
            print("Cart is empty. Cannot place an order.")
            return

        # Connect to your database
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()

        # Loop through cart items and insert each one into the orders table
        for _, name, price, qty in cart_items:
            total = float(price) * int(qty)  # Calculate total for each item
            discount = total * 0.20 if total > 1500 else 0  # Apply discount if total > 1500
            final_total = total - discount  # Calculate final total after discount

            # Insert data into the orders table
            cursor.execute("""
                INSERT INTO orders (cart_name, cart_qty, cart_price, total, discount, final_total)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, qty, price, total, discount, final_total))

        # Commit the transaction
        con.commit()

        # Clear the cart after placing the order
        clear_cart()

    except Exception as e:
        print("Error placing order:", e)
    finally:
        if con:
            con.close()

# Function to handle placing an order
def place_order_action():
    place_order()  # Insert cart data into orders table and clear the cart
    OrderMenu()  # Call the OrderMenu function to display updated orders

# Create a Treeview widget to display orders in the OrderMenu
def OrderMenu():
    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()

        # Fetch all orders from the orders table
        cursor.execute("""
            SELECT order_id, cart_name, cart_qty, cart_price, total, discount, final_total, order_date 
            FROM orders
        """)
        orders = cursor.fetchall()

        # Clear existing rows in the Treeview
        for row in treeview.get_children():
            treeview.delete(row)

        # Insert new rows for each order
        for order in orders:
            treeview.insert("", "end", values=order)

    except Exception as e:
        print("Error fetching orders:", e)
    finally:
        if con:
            con.close()

# Create the Place Order button and assign the action to it
MenuCartPlaceOrderBtn = Button(MenuCartTotalFrame, text="Place an order", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=place_order_action)
MenuCartPlaceOrderBtn.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)
