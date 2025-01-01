import mysql.connector
from tkinter import *
from tkinter import messagebox

# Database credentials
DB_HOST = "your_host"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "your_database"

# Function to handle placing an order
def place_order_action():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        # Fetch cart data
        cursor.execute("SELECT * FROM cart")
        cart_data = cursor.fetchall()

        if not cart_data:
            messagebox.showinfo("Info", "Your cart is empty!")
            return

        # Insert cart data into orders table
        for item in cart_data:
            cursor.execute(
                "INSERT INTO orders (product_id, quantity, price, user_id) VALUES (%s, %s, %s, %s)",
                (item[1], item[2], item[3], item[4])  # Adjust columns as per your database
            )

        # Clear the cart
        cursor.execute("DELETE FROM cart")
        conn.commit()

        # Show success message
        messagebox.showinfo("Success", "Your order has been placed successfully!")

        # Clear cart UI (if applicable)
        for widget in MenuCartFrame.winfo_children():
            widget.destroy()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Main Tkinter application
root = Tk()
root.title("Shopping Cart")
root.geometry("600x400")

# Colors
primary_color = "#3498db"
secondary_color = "#ffffff"
active_color = "#2980b9"

# Frame for cart
MenuCartFrame = Frame(root, bg="lightgray")
MenuCartFrame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.6)

# Mock Cart Data (Optional for Testing UI)
cart_items = ["Item 1", "Item 2", "Item 3"]
for index, item in enumerate(cart_items):
    Label(MenuCartFrame, text=item, font=("Arial", 12), bg="lightgray").place(relx=0.05, rely=0.1 * index)

# Frame for the "Place Order" button
MenuCartTotalFrame = Frame(root, bg="white")
MenuCartTotalFrame.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

# "Place Order" button
MenuCartPlaceOrderBtn = Button(
    MenuCartTotalFrame,
    text="Place an order",
    font=("century gothic bold", 13),
    background=primary_color,
    foreground=secondary_color,
    cursor="hand2",
    relief="flat",
    activebackground=active_color,
    bd=2,
    command=place_order_action
)
MenuCartPlaceOrderBtn.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)

# Start the Tkinter main loop
root.mainloop()
