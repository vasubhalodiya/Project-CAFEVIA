def add_to_cart(product_id, product_name, product_price):
    try:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()

        # Check if the product already exists in the cart
        cursor.execute("SELECT cartqty, cartprice FROM cart WHERE cartname = %s", (product_name,))
        cart_item = cursor.fetchone()

        if cart_item:
            # Update quantity if product already exists in cart
            new_qty = cart_item[0] + 1
            new_total = new_qty * product_price
            cursor.execute("UPDATE cart SET cartqty = %s, cartprice = %s WHERE cartname = %s", 
                           (new_qty, new_total, product_name))
        else:
            # Add new product to the cart
            cursor.execute("INSERT INTO cart (cartname, cartqty, cartprice) VALUES (%s, %s, %s)", 
                           (product_name, 1, product_price))

        con.commit()
        print(f"Added {product_name} to cart successfully!")

        # Immediately update the cart display after adding to cart
        populate_cart(cart_item_frame)  # Refresh the cart UI
        update_total()  # Update the total value after adding the product

    except Exception as e:
        print("Error while adding to cart:", e)
    finally:
        if con:
            con.close()
