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
                # Prevent going beyond the maximum quantity
                if new_qty < 1:
                    new_qty = 1
                if new_qty > 10:  # MAX_QUANTITY is set to 10
                    new_qty = 10

                try:
                    con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                    cursor = con.cursor()
                    cursor.execute("UPDATE cart SET cartqty = %s WHERE cartname = %s", (new_qty, cart_name))
                    con.commit()

                    # Immediately update the label with the new quantity in the UI
                    label_qty.config(text=str(new_qty))  # Update the quantity label immediately
                except Exception as e:
                    print("Error updating cart:", e)
                finally:
                    if con:
                        con.close()

            def populate_cart(frame):
                # Clear existing widgets
                for widget in frame.winfo_children():
                    widget.destroy()

                # Fetch cart data
                cart_items = fetch_cart_data()  # Ensure this returns (cart_id, name, qty, price)

                for idx, (cart_id, name, price, qty) in enumerate(cart_items):  # Ensure this order is correct
                    total = int(qty) * float(price)  # Calculate total dynamically

                    card = Frame(frame, background=sidecart_color)  # Adjust the background color as needed
                    card.place(relx=0.05, rely=0.16 + (idx * 0.12), relwidth=0.91, relheight=0.11)

                    # Product image (placeholder)
                    img = Image.open('images/coffee.png').resize((60, 60))
                    img = ImageTk.PhotoImage(img)
                    Label(card, image=img, bg=sidecart_color).place(relx=0, rely=0.09, width=75, height=75)
                    card.image = img  # Keep reference to avoid garbage collection

                    # Product details
                    MenuCartProductName = Label(card, text=name, bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13)).place(relx=0.3, rely=0.1)

                    # Price Label
                    MenuCartOrderPrice = Label(card, text=f"₹ {price}", bg=price_color, fg=secondary_color, font=("century gothic bold", 13)).place(relx=0.32, rely=0.5, relwidth=0.21, relheight=0.24)

                    # Quantity label (updated dynamically)
                    label_qty = Label(card, text=qty, bg=sidecart_color, fg=primary_color, font=("century gothic bold", 15))
                    label_qty.place(relx=0.7, rely=0.5, width=22, height=22)

                    # Quantity controls with red background for buttons
                    MenuCartMinusBtn = Button(card, text="-", font=("century gothic bold", 15), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda n=name, q=int(qty), p=float(price), label_qty=label_qty: update_cart(n, max(1, q - 1), p, label_qty)).place(relx=0.6, rely=0.5, width=25, height=25)

                    # Plus button for Quantity with red background
                    MenuCartPlusBtn = Button(card, text="+", font=("century gothic bold", 15), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda n=name, q=int(qty), p=float(price), label_qty=label_qty: update_cart(n, min(10, q + 1), p, label_qty)).place(relx=0.8, rely=0.5, width=25, height=25)

            populate_cart(MenuCartFrame)  # Load the cart