from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import MySQLdb
from tkinter import messagebox
import mysql.connector
import io
import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Canvas, Button, messagebox


primary_color = "#27150C"
secondary_color = "#E7E0D6"
sidecart_color = "#DDD2C3"
active_color = "#EDD6B3"
price_color = "#B26431"
# ============= Blue theme color ============
# primary_color = "#221D20"
# secondary_color = "#F3F3F3"
# sidecart_color = "#E0E3EB"
# active_color = active_color #not define
# price_color = price_color #not define
# card_color = "#E4E4E7" #or #E0E3EB
# cardimg_color = "#D7DAE2" #or #F3F3F3


# def loading_screen():
#     window = Tk()
#     width = 370
#     height = 230
#     x = (window.winfo_screenwidth()//2)-(width//2)
#     y = (window.winfo_screenheight()//2)-(height//2)
#     window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#     window.overrideredirect(True)
#     window.configure(bg=secondary_color)

#     # text = "CAFEVIA"
#     # spaced_text = " ".join(text)

#     loading_text = Label(window, text="CAFEVIA", font=("century gothic bold", 30), bg=secondary_color, fg=primary_color)
#     loading_text.place(relx=0.5, rely=0.5, anchor=CENTER)
    
#     def redirectToHome():
#         window.destroy()
#         AdminDashboard()

#     window.after(3000, redirectToHome)
#     window.mainloop()

# loading_screen()

class Login():
    def __init__(self,loginwindow):
        self.loginwindow = loginwindow
        self.loginwindow.title("LOGIN - CAFEVIA")
        width = 1000
        height = 600
        x = (loginwindow.winfo_screenwidth()//2)-(width//2)
        y = (loginwindow.winfo_screenheight()//2)-(height//2)
        self.loginwindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.loginwindow.state('normal')
        self.loginwindow.resizable(False, False)
        self.loginwindow.config(background=secondary_color)

        loginimage = Image.open('images/login_img.jpg')
        loginimage = ImageTk.PhotoImage(loginimage)
        loginimage_label = Label(self.loginwindow, image=loginimage,  background=secondary_color)
        loginimage_label.image = loginimage
        loginimage_label.place(relx=0, rely=0, relwidth=0.57, relheight=1)

        #Use Verification
        name_var = StringVar()
        passw_var = StringVar()

        loginform = Frame(loginwindow, background=secondary_color)
        loginform.place(relx=0.37, rely=0, relwidth=0.63, relheight=1)

        loginwindow.overrideredirect(True)
        def close_button():
            loginwindow.destroy() 
        closebutton = Button(loginform, text="x", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=close_button)
        closebutton.place(relx=0.94, rely=0.014, width=30, height=30)
        
        # login logo
        loginlogo = Label(loginform, text="CAFEVIA", bg=secondary_color, fg=primary_color, font=("century gothic bold", 30), bd=0)
        loginlogo.place(relx=0.35, rely=0.07)
        loginslogan = Label(loginform, text="Wake up, sip, and conquer your day with our brew.", bg=secondary_color, fg=primary_color, font=("century gothic", 10))
        loginslogan.place(relx=0.23, rely=0.15)

        loginUserlabel = Label(loginform, text="Username", bg=secondary_color, fg=primary_color, font=("century gothic bold", 16))
        loginUserlabel.place(relx=0.2, rely=0.3)
        txtProductName = Entry(loginform, textvariable="name_var", font=("century gothic", 13), relief='ridge', bd=2)
        txtProductName.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.065)

        loginPasswordlabel = Label(loginform, text="Password", bg=secondary_color, fg=primary_color, font=("century gothic bold", 16))
        loginPasswordlabel.place(relx=0.2, rely=0.46)
        loginPasswordentry = Entry(loginform, textvariable="passw_var", font=("century gothic", 13), relief='ridge', bd=2, show='*')
        loginPasswordentry.place(relx=0.2, rely=0.51, relwidth=0.6, relheight=0.065)

        login = Button(loginform, text="Login", font=("century gothic bold", 15), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", bd=2, command=submit)
        login.place(relx=0.2, rely=0.68, relwidth=0.6, relheight=0.065)
        loginNote = Label(loginform, text="Must do check USERNAME & PASSWORD is correct", bg=secondary_color, fg=primary_color, font=("century gothic", 8))
        loginNote.place(relx=0.2, rely=0.755, relwidth=0.6, relheight=0.015)

        def Submit(name, passv):
            mylabel = Label(loginform, text = name + passv).pack()

def submit():
    loginwindow.destroy()
    win()


class AdminDashboard():
    def __init__(self,window):
        self.window = window
        self.window.title("CAFEVIA")
        # self.window.geometry("1500x750")
        self.window.state('zoomed')
        self.window.resizable(False, False)
        self.window.config(background=secondary_color)

        # sidebar
        self.sidebar = Frame(self.window, bg=primary_color)
        self.sidebar.place(relx=0, rely=0, relwidth=0.18, relheight=1) 

        # logoimage = Image.open('images/logo.png').resize((60, 60))
        # logoimage = ImageTk.PhotoImage(logoimage)
        # logoimage_label = Label(self.sidebar, image=logoimage, background=primary_color)
        # logoimage_label.image = logoimage
        # logoimage_label.place(relx=0, rely=0.09, width=75, height=75)
        text = "CAFEVIA"
        spaced_text = " ".join(text)

        loading_text = Label(self.sidebar, text=spaced_text, font=("century gothic bold", 27), bg=primary_color, fg=secondary_color)
        loading_text.place(relx=0.1, rely=0.07)

        # Dashboard Button

        DashboardButton = Button(self.sidebar, text="Dashboard", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(DashboardMenu))
        DashboardButton.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.05)

        MenuButton = Button(self.sidebar, text="Menu", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(MenuMenu))
        MenuButton.place(relx=0.1, rely=0.28, relwidth=0.8, relheight=0.05)

        BillingButton = Button(self.sidebar, text="Billing", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(BillingMenu))
        BillingButton.place(relx=0.1, rely=0.36, relwidth=0.8, relheight=0.05)

        OrderButton = Button(self.sidebar, text="Orders", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(OrderMenu))
        OrderButton.place(relx=0.1, rely=0.44, relwidth=0.8, relheight=0.05)

        TableBookButton = Button(self.sidebar, text="Table Book", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(TableBookMenu))
        TableBookButton.place(relx=0.1, rely=0.52, relwidth=0.8, relheight=0.05)

        SalesButton = Button(self.sidebar, text="Sales", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(SalesMenu))
        SalesButton.place(relx=0.1, rely=0.60, relwidth=0.8, relheight=0.05)

        LogoutButton = Button(self.sidebar, text="Logout", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(LogoutMenu))
        LogoutButton.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.05)

        # Functionality for menu system
        main_frame = Frame(window, background=secondary_color)
        main_frame.place(relx=0.18, rely=0, relwidth=0.82, relheight=1)

        HomeImage = Image.open('images/homeimg.jpg')
        HomeImage = ImageTk.PhotoImage(HomeImage)
        HomeImage_label = Label(main_frame, image=HomeImage, background=sidecart_color)
        HomeImage_label.image = HomeImage
        HomeImage_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.HomeLabel = Label(main_frame, text="Welcome to CAFEVIA", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 25))
        self.HomeLabel.place(relx=0.35, rely=0.18)

# ===========================================================================================

        def MenuSystem(page):
            for frame in main_frame.winfo_children():
                frame.destroy()
            page()

        def DashboardMenu():
            DashboardFrame = Frame(main_frame, background=secondary_color)
            DashboardFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

            txtDashboard = Label(DashboardFrame, text="Dashboard", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            txtDashboard.place(relx=0.03, rely=0.02)


           # Connect to MySQL Database
            def get_db_connection():
                return mysql.connector.connect(
                    host="localhost",  
                    user="root",       
                    password="",
                    database="cafevia"
                )

            # Fetch row count for a specific table
            def get_table_row_count(table_name):
                try:
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                    row_count = cursor.fetchone()[0]
                    conn.close()
                    return row_count
                except mysql.connector.Error as err:
                    print(f"Error fetching data from table '{table_name}': {err}")
                    return 0  # Return 0 if there's an error (e.g., table doesn't exist)

            # Create a card with dynamic data
            def create_card(frame, title, value, icon_path, x, y):
                card = Frame(frame, background=sidecart_color)
                card.place(relx=x, rely=y, relwidth=0.22, relheight=0.18)

                # Title label
                Label(card, text=title, bg=sidecart_color, fg="black", font=("Arial", 12)).place(relx=0.08, rely=0.25)
                
                # Value label
                Label(card, text=value, bg=sidecart_color, fg="black", font=("Arial", 25, 'bold')).place(relx=0.08, rely=0.45)
                
                # Icon
                try:
                    icon = Image.open(icon_path).convert("RGBA")
                    # Reduce opacity to 70%
                    alpha = icon.getchannel("A")  # Get the alpha channel
                    alpha = alpha.point(lambda p: int(p * 0.7))  # Apply 70% opacity
                    icon.putalpha(alpha)  # Set the modified alpha channel back to the image
                    # Resize and convert to Tkinter-compatible format
                    icon = icon.resize((60, 60))
                    icon = ImageTk.PhotoImage(icon)
                    # Create icon label and set the image
                    icon_label = Label(card, image=icon, bg=sidecart_color)
                    icon_label.image = icon
                    icon_label.place(relx=0.67, rely=0.28, width=60, height=60)
                    
                except Exception as e:
                    print(f"Error loading icon for {title}: {e}")

            # Cards data dynamically fetched from the database
            cards_data = [
                {"title": "Happy Customers", "table_name": "customers", "icon_path": "images/happycustomer.png"},
                {"title": "All Category", "table_name": "category", "icon_path": "images/category.png"},
                {"title": "All Products", "table_name": "product", "icon_path": "images/product.png"},
                {"title": "Available Tables", "table_name": "tables", "icon_path": "images/tablebook.png"},
                {"title": "All Orders", "table_name": "orders", "icon_path": "images/order.png"},
                {"title": "Total Sales", "value": "$ 10,000", "icon_path": "images/sales.png"},
            ]

            # Constants for layout
            cards_per_row = 4  # Maximum cards per row
            card_width = 0.22  # Width of each card
            card_height = 0.18  # Height of each card
            horizontal_spacing = 0.02  # Spacing between cards
            vertical_spacing = 0.03  # Spacing between rows

            # Starting position for the first card
            start_relx = 0.03
            start_rely = 0.1

            # Loop to create dashboard cards
            for idx, card in enumerate(cards_data):
                # Fetch the row count from the database if it exists
                if 'table_name' in card:
                    row_count = get_table_row_count(card["table_name"])
                    card["value"] = str(row_count)  # Update the card with the dynamic value
                
                # Calculate relx and rely for dynamic positioning
                col = idx % cards_per_row
                row = idx // cards_per_row

                relx = start_relx + col * (card_width + horizontal_spacing)
                rely = start_rely + row * (card_height + vertical_spacing)

                # Create the card using the `create_card` function
                create_card(DashboardFrame, card["title"], card["value"], card["icon_path"], relx, rely)

        # ==========================================

        def MenuMenu():
            MenuFrame = Frame(main_frame, background=secondary_color)
            MenuFrame.place(relx=0, rely=0, relwidth=0.8, relheight=1)

        # ================== Menu Cart Product Start=====================
            MenuCartFrame = Frame(main_frame, background=sidecart_color)
            MenuCartFrame.place(relx=0.76, rely=0, relwidth=0.24, relheight=1)

            cart_item_frame = Frame(main_frame, background=sidecart_color)
            cart_item_frame.place(relx=0.76, rely=0.15, relwidth=0.24, relheight=0.6)

        # ===================================================
        
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

                    # Image
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
                    Button(card, text="X", font=("century gothic bold", 10), bg="red", fg=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda n=name, card=card: remove_from_cart(n, card)).place(relx=0.85, rely=0.02, width=22, height=22)
                    

            # Assuming you have a frame for cart items
            populate_cart(cart_item_frame)


        # ============================

            MenuCartItem = Label(MenuCartFrame, text="Cart", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 20))
            MenuCartItem.place(relx=0.03, rely=0.01)

            MenuCartOrderNo = Label(MenuCartFrame, text="Order #3243", bg=sidecart_color, fg=primary_color, font=("century gothic", 10))
            MenuCartOrderNo.place(relx=0.7, rely=0.02)

            MenuCartDineInBtn = Button(MenuCartFrame, text="Dine In", font=("century gothic bold", 11), background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            MenuCartDineInBtn.place(relx=0.05, rely=0.07, relwidth=0.25, relheight=0.04)

            MenuCartTakeAwayBtn = Button(MenuCartFrame, text="Take away", font=("century gothic bold", 11), background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            MenuCartTakeAwayBtn.place(relx=0.35, rely=0.07, relwidth=0.35, relheight=0.04)

        # ===================================================

            # Define the labels globally and place them in the frame
            MenuCartItemTotal = Label(MenuCartFrame, text="Items", bg=sidecart_color, fg=primary_color, font=("century gothic", 11), anchor="w")
            MenuCartItemTotal.place(relx=0.05, rely=0.77, relwidth=0.2, relheight=0.03)

            MenuCartItemTotalAns = Label(MenuCartFrame, text="₹ 0", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 12), anchor="e")
            MenuCartItemTotalAns.place(relx=0.7, rely=0.77, relwidth=0.25, relheight=0.03)

            MenuCartDiscountTotal = Label(MenuCartFrame, text="Discount", bg=sidecart_color, fg=primary_color, font=("century gothic", 11), anchor="w")
            MenuCartDiscountTotal.place(relx=0.05, rely=0.81, relwidth=0.25, relheight=0.03)

            MenuCartDiscountTotalAns = Label(MenuCartFrame, text="-₹ 0", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 12), anchor="e")
            MenuCartDiscountTotalAns.place(relx=0.68, rely=0.81, relwidth=0.27, relheight=0.03)

            # *************
            MenuCartTotalFrame = Frame(MenuCartFrame, background=sidecart_color)
            MenuCartTotalFrame.place(relx=0.05, rely=0.86, relwidth=0.9, relheight=0.14)
            top_border = Frame(MenuCartTotalFrame, bg="#CBA084", height=1)
            top_border.pack(side="top", fill="x")
            # *************
            MenuCartAllTotal = Label(MenuCartTotalFrame, text="Total", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 12), anchor="w")
            MenuCartAllTotal.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.2)

            # Add MenuCartAllTotalAns for the final total
            MenuCartAllTotalAns = Label(MenuCartTotalFrame, text="₹ 0", bg=price_color, fg=secondary_color, font=("century gothic bold", 12))
            MenuCartAllTotalAns.place(relx=0.73, rely=0.2, relwidth=0.28, relheight=0.2)


            # Function to update total and discount
            def update_total():
                # Fetch cart data from database
                cart_items = fetch_cart_data()  # Fetch all cart items (cart_id, name, qty, price)

                total = 0  # Variable to store the total price
                for _, name, price, qty in cart_items:
                    total += float(price) * int(qty)  # Calculate total for each item

                # Calculate discount based on total
                discount = total * 0.20 if total > 800 else 0  # 20% discount if total > 1500, else 0% discount
                final_total = total - discount  # Final total after applying discount

                # Update the total price label
                MenuCartItemTotalAns.config(text=f"₹ {total:.0f}")
                MenuCartDiscountTotalAns.config(text=f"- ₹ {discount:.0f}")
                MenuCartAllTotalAns.config(text=f"₹ {final_total:.0f}")

            # Call this function after updating the cart or when populating the cart
            update_total()

            # Function to open the customer name frame
            def open_customer_name_frame():
                customer_frame = Toplevel()
                customer_frame.title("Customer Details")
                customer_frame.geometry("300x150")
                customer_frame.resizable(False, False)

                Label(customer_frame, text="Enter Customer Name:", font=("century gothic", 12)).pack(pady=10)

                customer_name_var = StringVar()
                Entry(customer_frame, textvariable=customer_name_var, font=("century gothic", 12), width=30).pack(pady=5)

                def submit_customer_name():
                    customer_name = customer_name_var.get()
                    if not customer_name.strip():
                        print("Customer name is required.")
                        return
                    place_order_action(customer_name)
                    customer_frame.destroy()

                Button(customer_frame, text="Submit", font=("century gothic bold", 12), bg=primary_color, fg=secondary_color, relief="flat", cursor="hand2", command=submit_customer_name).pack(pady=10)

            # Function to place an order
            def place_order_action(customer_name):
                try:
                    con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                    cursor = con.cursor()
                    cart_items = fetch_cart_data()
                    if not cart_items:
                        print("Cart is empty.")
                        return
                    for _, name, price, qty in cart_items:
                        cursor.execute("INSERT INTO orders (ordername, orderqty, orderprice, customername) VALUES (%s, %s, %s, %s)", (name, qty, price, customer_name))
                    cursor.execute("DELETE FROM cart")
                    con.commit()
                    populate_cart(cart_item_frame)
                    update_total()
                except Exception as e:
                    print("Error placing order:", e)
                finally:
                    if con:
                        con.close()

            MenuCartPlaceOrderBtn = Button(MenuCartTotalFrame, text="Place an order", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=open_customer_name_frame)
            MenuCartPlaceOrderBtn.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)



        # ================== Menu Cart Product End=====================

            categories = [
                {"name": "All", "image": "images/all.png"},
                {"name": "Coffee", "image": "images/coffee.png"},
                {"name": "Softdrink", "image": "images/softdrink.png"},
                {"name": "Pizza", "image": "images/pizza.png"},
                {"name": "Burger", "image": "images/burger.png"},
                {"name": "Dessert", "image": "images/dessert.png"},
                {"name": "Food Meal", "image": "images/meal.png"},
            ]

           # Label for choosing category
            ChooseCategory = Label(MenuFrame, text="Choose Category", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            ChooseCategory.place(relx=0.03, rely=0.02)

            # Function to filter products by category
            def filter_products_by_category(category_name):
                # Clear the existing product cards
                for widget in canvas_frame.winfo_children():
                    widget.destroy()

                # Fetch products based on the selected category
                con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                cursor = con.cursor()

                # If "All" is selected, fetch all products
                if category_name == "All":
                    cursor.execute("SELECT * FROM product")
                else:
                    cursor.execute("SELECT * FROM product WHERE procategory = %s", (category_name,))

                products = cursor.fetchall()
                con.close()

                # Display the filtered products
                card_count = 0
                row_frame = None
                for product_details in products:
                    if card_count % 4 == 0:
                        row_frame = Frame(canvas_frame, background=secondary_color)
                        row_frame.pack(padx=20, pady=10)

                    ProductDtlCard = Frame(row_frame, background=sidecart_color, width=200, height=210)
                    ProductDtlCard.grid(row=0, column=card_count % 4, padx=15)

                    ProductImageFrame = Frame(ProductDtlCard, background=sidecart_color, width=200, height=210)
                    ProductImageFrame.place(relx=0.27, rely=0.01)

                    # Image
                    product_id = product_details[0]  # Assuming the product ID is in the first column (index 0)
                    product_image = fetch_image(product_id)
                    if product_image:
                        label = tk.Label(ProductImageFrame, image=product_image, background=sidecart_color)
                        label.image = product_image
                        label.pack(pady=10)

                    # Category
                    ProductCategoryLabel = Label(ProductDtlCard, text=product_details[3], bg=sidecart_color, fg=primary_color, font=("century gothic", 8), anchor="w")
                    ProductCategoryLabel.place(relx=0.05, rely=0.56, relwidth=0.32, relheight=0.09)

                    # Product Name
                    ProductNameLabel = Label(ProductDtlCard, text=product_details[2], bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13), anchor="w")
                    ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)

                    # Price
                    ProductPriceLabel = Label(ProductDtlCard, text=f"₹ {product_details[4]}", bg=price_color, fg=sidecart_color, font=("century gothic bold", 15))
                    ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)

                    # Add to Cart Button
                    product_name = product_details[2]  # Assuming product name is in column index 2
                    product_price = product_details[4]  # Assuming product price is in column index 4
                    ProductAddToCardButton = Button(ProductDtlCard, text="Add", font=("century gothic bold", 11), width=27, height=1, background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda pid=product_id, pname=product_name, pprice=product_price: add_to_cart(pid, pname, pprice))
                    ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)

                    card_count += 1

            # Function to fetch image for each product by product ID
            def fetch_image(product_id):
                con = mysql.connector.connect(host="localhost", user="root", password="", database="cafevia")
                cursor = con.cursor()
                cursor.execute("SELECT proimage FROM product WHERE proid = %s", (product_id,))
                image_data = cursor.fetchone()
                con.close()

                if image_data:
                    img = Image.open(io.BytesIO(image_data[0]))  # Assuming image is the first column
                    img = img.resize((90, 90))  # Resize image as needed
                    return ImageTk.PhotoImage(img)
                return None

            # Function to insert data into the cart table
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
                        cursor.execute("UPDATE cart SET cartqty = %s, cartprice = %s WHERE cartname = %s", (new_qty, new_total, product_name))
                    else:
                        # Add new product to the cart
                        cursor.execute("INSERT INTO cart (cartname, cartqty, cartprice) VALUES (%s, %s, %s)", (product_name, 1, product_price))

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


            # Create category buttons
            for i, category in enumerate(categories):
                category_image = Image.open(category["image"]).resize((45, 45))
                category_image = ImageTk.PhotoImage(category_image)
                
                relx = 0.03 + i * 0.13
                
                CategoryChildCard = Button(MenuFrame, text=category["name"], image=category_image, background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, compound="top", font=("century gothic bold", 12), pady=13, command=lambda cat=category["name"]: filter_products_by_category(cat))
                CategoryChildCard.image = category_image
                CategoryChildCard.place(relx=relx, rely=0.08, width=110, height=110)

            # Add Coffee Category
            CoffeeCategory = Frame(MenuFrame, background=secondary_color)
            CoffeeCategory.place(relx=0, rely=0.27, relwidth=0.95, relheight=1)
            CoffeeCategoryLabel = Label(CoffeeCategory, text="Coffee Menu", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            CoffeeCategoryLabel.place(relx=0.03, rely=0.02)

            # Add Product Button
            AddProductButton = Button(CoffeeCategory, text="Add Product", background=primary_color, foreground=secondary_color, cursor="hand2", relief="solid", activebackground=active_color, bd=0, font=("century gothic bold", 12), command=ProductMenu)
            AddProductButton.place(relx=0.815, rely=0.02, relwidth=0.15, relheight=0.05)

            # Add a scrollbar to the ProductCategorymain_frame
            ProductCategorymain_frame = Frame(CoffeeCategory)
            ProductCategorymain_frame.place(relx=0, rely=0.08, relwidth=1, relheight=0.66)

            # Create a Canvas inside the ProductCategorymain_frame
            product_canvas = Canvas(ProductCategorymain_frame, bg=secondary_color, bd=0, highlightthickness=0)
            product_canvas.pack(side="left", fill="both", expand=True)

            # Create a vertical scrollbar
            scrollbar = Scrollbar(ProductCategorymain_frame, orient="vertical", command=product_canvas.yview)
            scrollbar.place(relx=0.988, rely=0, relwidth=0.013, relheight=1)

            # Configure the canvas to use the scrollbar
            product_canvas.configure(yscrollcommand=scrollbar.set)

            # Create a frame inside the canvas to hold the content
            canvas_frame = Frame(product_canvas, background=secondary_color)
            product_canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

            # Bind the canvas to resize the scroll region
            def update_scrollregion(event):
                product_canvas.configure(scrollregion=product_canvas.bbox("all"))

            canvas_frame.bind("<Configure>", update_scrollregion)

            # Add mousewheel scrolling functionality
            def on_mousewheel(event):
                product_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

            product_canvas.bind_all("<MouseWheel>", on_mousewheel)

            # Initially display products from "All" category after canvas_frame is created
            filter_products_by_category("All")


# =========================================================================================================

        def ProductMenu():
            AddCoffeeWindow = Tk()
            AddCoffeeWindow.title("Add Coffee - CAFEVIA")
            width = 1200
            height = 750
            x = (AddCoffeeWindow.winfo_screenwidth() // 2) - (width // 2)
            y = (AddCoffeeWindow.winfo_screenheight() // 2) - (height // 2)
            AddCoffeeWindow.geometry(f'{width}x{height}+{x}+{y}')
            AddCoffeeWindow.resizable(False, False)
            AddCoffeeWindow.config(background=secondary_color)
            # AddCoffeeWindow.attributes("-topmost", True)

            def browse_image():
                # Open a file dialog to allow the user to select an image file.
                global selected_file_path
                selected_file_path = filedialog.askopenfilename(
                    title="Select Image",
                    filetypes=[("Image Files", ".png;.jpg;.jpeg;.bmp;*.gif")]
                )
                if selected_file_path:
                    messagebox.showinfo("File Selected", f"Image selected: {selected_file_path}")
                else:
                    messagebox.showerror("Error", "No image selected.")



            def Productinsert():
                # Insert movie details along with an optional image into the database.
                global selected_file_path

                ProductName = txtProductName.get()
                ProductCategory = txtProductCategory.get()
                ProductPrice = txtProductPrice.get()
                # ProductImage = txtProductImage.get()

                if (ProductName=="" or ProductCategory=="" or ProductPrice==""):
                    messagebox.showinfo("Insert Status","All fields are required")
                    return  # Exit the function if validation fails

                # Read the selected image file
                image_data = None
                if selected_file_path:
                    try:
                        with open(selected_file_path, "rb") as file:
                            image_data = file.read()
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to read image file: {str(e)}")
                        return

                try:
                    # Connect to the database
                    con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                    cursor = con.cursor()

                    # SQL query to insert movie details along with the image
                    query = """ INSERT INTO product (proname, procategory, proprice, proimage) VALUES (%s, %s, %s, %s) """
                    values = (ProductName, ProductCategory, ProductPrice, image_data if image_data else None)

                    cursor.execute(query, values)
                    con.commit()

                    # Clear input fields and reset the image path
                    txtProductName.delete(0,'end')
                    txtProductCategory.delete(0,'end')
                    txtProductPrice.delete(0,'end')
                    selected_file_path = None  # Reset the global variable

                    # Success message
                    messagebox.showinfo("INSERT Status", "INSERTED SUCCESSFULLY")

                except MySQLdb.OperationalError as e:
                    messagebox.showerror("Database Error", f"Operational error: {str(e)}")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                finally:
                    con.close()


            def ProductDelete():
                if(txtProductId.get() == ""):
                    messagebox.showinfo("Delete Status", "ID is required for delete operation")
                else:
                    try:
                        # Connect to the database
                        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                        cursor = con.cursor()

                        # query = "DELETE FROM product WHERE proid = %s"
                        cursor.execute("delete from product where proid='"+txtProductId.get()+"'")
                        con.commit()

                        txtProductId.delete(0, 'end')
                        txtProductName.delete(0, 'end')
                        txtProductCategory.delete(0, 'end')
                        txtProductPrice.delete(0, 'end')

                        messagebox.showinfo("DELETE Status", "Deleted Successfully")
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred: {str(e)}")
                    con.close()

            def ProductUpdate():
                ProductId = txtProductId.get()
                ProductName = txtProductName.get()
                ProductCategory = txtProductCategory.get()
                ProductPrice = txtProductPrice.get()

                if (ProductId=="" or ProductName=="" or ProductCategory=="" or ProductPrice==""):
                    messagebox.showinfo("Update Status", "All fields are required")
                else:
                    try:
                        # Connect to the database
                        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                        cursor = con.cursor()

                        cursor.execute("update product set proname='"+txtProductName.get()+"',procategory='"+txtProductCategory.get()+"',proprice='"+txtProductPrice.get()+"' where proid='"+txtProductId.get()+"'")
                        con.commit()

                        # Clear input fields
                        txtProductId.delete(0, 'end')
                        txtProductName.delete(0, 'end')
                        txtProductCategory.delete(0, 'end')
                        txtProductPrice.delete(0, 'end')
                        messagebox.showinfo("UPDATE Status", "UPDATED SUCCESSFULLY")

                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred: {str(e)}")
                    con.close()

            AddNavbar = Frame(AddCoffeeWindow, background=primary_color)
            AddNavbar.place(relx=0, rely=0, relwidth=1, relheight=0.5)

            AddHeadLabel = Label(AddCoffeeWindow, text="Add Coffee", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            AddHeadLabel.place(relx=0, rely=0.02, relwidth=1, relheight=0.05)

            lblProductId = Label(AddCoffeeWindow, text="Product Id", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductId.place(relx=0.07, rely=0.1)
            txtProductId = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductId.place(relx=0.07, rely=0.15, relwidth=0.25, relheight=0.05)

            lblProductCategory = Label(AddCoffeeWindow, text="Product Category", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductCategory.place(relx=0.07, rely=0.23)
            txtProductCategory = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductCategory.place(relx=0.07, rely=0.28, relwidth=0.25, relheight=0.05)

            lblProductName = Label(AddCoffeeWindow, text="Product Name", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductName.place(relx=0.4, rely=0.1)
            txtProductName = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductName.place(relx=0.4, rely=0.15, relwidth=0.25, relheight=0.05)

            lblProductPrice = Label(AddCoffeeWindow, text="Product Price", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductPrice.place(relx=0.4, rely=0.23)
            txtProductPrice = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductPrice.place(relx=0.4, rely=0.28, relwidth=0.25, relheight=0.05)

            lblProductImage = Label(AddCoffeeWindow, text="Product Image", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductImage.place(relx=0.07, rely=0.36)
            txtProductImage = Button(AddCoffeeWindow, text="Browse Image", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=browse_image)
            txtProductImage.place(relx=0.07, rely=0.41, relwidth=0.25, relheight=0.05)

            AddProductButton = Button(AddCoffeeWindow, text="Add Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=Productinsert)
            AddProductButton.place(relx=0.73, rely=0.12, relwidth=0.2, relheight=0.08)

            EditProductButton = Button(AddCoffeeWindow, text= "Edit Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=ProductUpdate)
            EditProductButton.place(relx=0.73, rely=0.24, relwidth=0.2, relheight=0.08)

            DeleteProductButton = Button(AddCoffeeWindow, text="Delete Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=ProductDelete)
            DeleteProductButton.place(relx=0.73, rely=0.36, relwidth=0.2, relheight=0.08)

            CRUDtxtDatagridView = Frame(AddCoffeeWindow,background=secondary_color)
            CRUDtxtDatagridView.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

            def fetch_data():
                try:
                    conn = MySQLdb.connect(
                        host="localhost",   # Replace with your database host
                        user="root",  # Replace with your username
                        password="",  # Replace with your password
                        database="cafevia"  # Replace with your database name
                    )
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM product")
                    rows = cursor.fetchall()
                    for count, row in enumerate(rows):
                        my_tree.insert(parent='', index='end', iid=count, text="", values=row)
                    conn.close()
                except MySQLdb.Error as err:
                    print(f"Error: {err}")
            my_tree = ttk.Treeview(CRUDtxtDatagridView)
            my_tree['columns'] = ("proid", "proimage", "proname","procategory","proprice")

            my_tree.column("#0", width=0, stretch=NO)  # Default column for the tree structure
            my_tree.column("proid", anchor="w", width=100)
            my_tree.column("proimage", anchor="w", width=440)
            my_tree.column("proname", anchor="w", width=220)
            my_tree.column("procategory", anchor="w", width=220)
            my_tree.column("proprice", anchor="w", width=220)

            my_tree.heading("#0", text="Label", anchor="w")
            my_tree.heading("proid", text="Product Id", anchor="w")
            my_tree.heading("proimage", text="Product Image", anchor="w")
            my_tree.heading("proname", text="Product Name", anchor="w")
            my_tree.heading("procategory", text="Product Ctegory", anchor="w")
            my_tree.heading("proprice", text="Product Price", anchor="w")

            def selectedrecord(e):
                txtProductId.delete(0, 'end')
                txtProductName.delete(0, 'end')
                txtProductCategory.delete(0, 'end')
                txtProductPrice.delete(0, 'end')

                selected = my_tree.focus()
                values = my_tree.item(selected,'values')

                txtProductId.insert(0,values[0])
                txtProductName.insert(0,values[2])
                txtProductCategory.insert(0,values[3])
                txtProductPrice.insert(0,values[4])

            my_tree.pack()  
            my_tree.bind("<ButtonRelease-1>",selectedrecord)
            fetch_data()


        # ==========================================

        def BillingMenu():
            BillingFrame = Frame(main_frame, background='green')
            BillingFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ==========================================

        def OrderMenu():
            OrderFrame = Frame(main_frame, background=secondary_color)
            OrderFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

            OrderHeading = Label(OrderFrame, text="Recent Orders", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            OrderHeading.place(relx=0.03, rely=0.02)

            # Function to fetch order data
            def fetch_order_data():
                try:
                    # Connect to the database
                    con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                    cursor = con.cursor()
                    
                    # Query the orders table
                    cursor.execute("SELECT * FROM orders")
                    data = cursor.fetchall()
                    return data
                except Exception as e:
                    print("Error fetching order data:", e)
                    return []
                finally:
                    if con:
                        con.close()

            # Function to populate Treeview
            def populate_treeview(tree):
                # Clear existing data
                for row in tree.get_children():
                    tree.delete(row)
                
                # Fetch data from the database
                orders = fetch_order_data()
                
                # Insert data into the Treeview
                for order in orders:
                    tree.insert("", "end", values=order)

            # Create a frame for the Treeview (occupying half the page)
            treeview_frame = Frame(OrderFrame, background="#f0f0f0")  # Adjust background if needed
            treeview_frame.place(relx=0.03, rely=0.09, relwidth=0.94, relheight=0.87)

            # Define columns for the Treeview
            columns = ("Order ID", "Order Name", "Customer Name", "Quantity", "Price", 
                    "Total", "Discount", "Final Total", "Order Date")

            # Style configuration for Treeview
            style = ttk.Style()
            style.configure("Custom.Treeview", background="#e6f2ff", fieldbackground="#e6f2ff", foreground=primary_color, rowheight=25)
            style.configure("Custom.Treeview.Heading", background="#white", foreground=primary_color, font=("Arial", 10, "bold"))

            # Create the Treeview widget with custom style
            tree = ttk.Treeview(treeview_frame, columns=columns, show="headings", height=10, style="Custom.Treeview")

            # Configure Treeview columns
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=130, anchor="center")  # Adjust column width as needed

            # Add a vertical scrollbar
            scrollbar = ttk.Scrollbar(treeview_frame, orient=VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Hide the scrollbar (still functional, but not visible)
            scrollbar.pack_forget()

            # Pack the Treeview widget
            tree.pack(fill=BOTH, expand=True)

            # Populate the Treeview with data
            populate_treeview(tree)



        # ==========================================

        def TableBookMenu():
            TableBookFrame = Frame(main_frame, background=secondary_color)
            TableBookFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

            btnTableAvaliavleIndicator = Button(TableBookFrame, bg=primary_color, relief="flat")
            btnTableAvaliavleIndicator.place(relx=0.035, rely=0.087, width=10, height=10)
            lblTableAvaliavleIndicator = Label(TableBookFrame, text="Avaliable", bg=secondary_color, fg=primary_color, font=("century gothic", 10))
            lblTableAvaliavleIndicator.place(relx=0.047, rely=0.08)

            btnTableAvaliavleIndicator = Button(TableBookFrame, bg="#F02533", relief="flat")
            btnTableAvaliavleIndicator.place(relx=0.12, rely=0.087, width=10, height=10)
            lblTableAvaliavleIndicator = Label(TableBookFrame, text="Reserved", bg=secondary_color, fg=primary_color, font=("century gothic", 10))
            lblTableAvaliavleIndicator.place(relx=0.133, rely=0.08)

            lblTable = Label(TableBookFrame, text="Table Booking", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            lblTable.place(relx=0.03, rely=0.02)

            # Database connection setup
            db = mysql.connector.connect(
                host="localhost",
                user="root",  # Replace with your MySQL username
                password="",  # Replace with your MySQL password
                database="cafevia"  # Updated database name
            )

            cursor = db.cursor()

            # Fetch table status from the database
            def get_table_status(table_number):
                cursor.execute("SELECT status FROM tablebook WHERE table_number = %s", (table_number,))
                result = cursor.fetchone()
                return result[0] if result else "available"

            # Update table status in the database
            def update_table_status(table_number, status):
                cursor.execute("UPDATE tablebook SET status = %s WHERE table_number = %s", (status, table_number))
                db.commit()

            def on_table_click(table_number):
                current_status = get_table_status(table_number)
                new_status = "reserved" if current_status == "available" else "available"
                update_table_status(table_number, new_status)
                
                # Fetch updated status
                status = get_table_status(table_number)
                
                # Update button color
                button_color = primary_color if status == "available" else "#F02533"  # Red color for reserved
                
                # Update chair color
                chair_color = price_color if status == "available" else "#CECECE"  # Grey color for reserved
                
                # Find the corresponding button and update its color
                for widget in canvas.winfo_children():
                    if isinstance(widget, Button) and widget.cget("text") == f"Table {table_number}":
                        widget.config(bg=button_color)
                        break
                
                # Change chair colors for the corresponding table
                for chair in canvas.find_withtag(f"table_{table_number}_chair"):
                    canvas.itemconfig(chair, fill=chair_color)
                
                messagebox.showinfo("Table Status Changed", f"Table {table_number} is now {new_status.capitalize()}!")

            def draw_table_with_chairs(canvas, relx, rely, table_width, table_height, chair_config, table_number):
                canvas_width = canvas.winfo_width()
                canvas_height = canvas.winfo_height()
                
                # Calculate the absolute position based on relative position
                x = relx * canvas_width
                y = rely * canvas_height
                
                # Fetch table status for coloring
                status = get_table_status(table_number)
                button_color = primary_color if status == "available" else "#F02533" # Red color for reserved
                chair_color = price_color if status == "available" else "#CECECE"  # Grey color for reserved
                
                # Table button
                table_button = Button(canvas, text=f"Table {table_number}", bg=button_color, fg=secondary_color, command=lambda: on_table_click(table_number), relief="flat")
                table_button.place(x=x, y=y, width=table_width, height=table_height)
                
                # Chair size and spacing
                chair_size = 20
                chair_spacing = 10
                
                # Draw chairs and add tags for chair elements
                # Draw chairs on the top side
                for i in range(chair_config["top"]):
                    chair_x = x + (i + 0.5) * (table_width / chair_config["top"]) - (chair_size / 2)
                    chair_y = y - chair_size - chair_spacing
                    chair = canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=chair_color, tags=f"table_{table_number}_chair")
                
                # Draw chairs on the bottom side
                for i in range(chair_config["bottom"]):
                    chair_x = x + (i + 0.5) * (table_width / chair_config["bottom"]) - (chair_size / 2)
                    chair_y = y + table_height + chair_spacing
                    chair = canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=chair_color, tags=f"table_{table_number}_chair")
                
                # Draw chairs on the left side
                for i in range(chair_config["left"]):
                    chair_x = x - chair_size - chair_spacing
                    chair_y = y + (i + 0.5) * (table_height / chair_config["left"]) - (chair_size / 2)
                    chair = canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=chair_color, tags=f"table_{table_number}_chair")
                
                # Draw chairs on the right side
                for i in range(chair_config["right"]):
                    chair_x = x + table_width + chair_spacing
                    chair_y = y + (i + 0.5) * (table_height / chair_config["right"]) - (chair_size / 2)
                    chair = canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=chair_color, tags=f"table_{table_number}_chair")

            # Create Canvas
            canvas = Canvas(TableBookFrame, bg=secondary_color, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)

            def draw_tables():
                # Draw tables with different configurations
                # ---------------------------- x, y, width, height -----------------------------
                # Row 1
                draw_table_with_chairs(canvas, 70, 50, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 1)   # Table 1
                draw_table_with_chairs(canvas, 290, 50, 150, 90, {"top": 3, "bottom": 3, "left": 2, "right": 2}, 2)  # Table 2
                draw_table_with_chairs(canvas, 560, 50, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 3)  # Table 3
                draw_table_with_chairs(canvas, 790, 50, 180, 90, {"top": 4, "bottom": 4, "left": 2, "right": 2}, 4)  # Table 4
                draw_table_with_chairs(canvas, 1080, 50, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 5) # Table 5

                # Row 2
                draw_table_with_chairs(canvas, 70, 290, 150, 90, {"top": 3, "bottom": 3, "left": 1, "right": 1}, 6)   # Table 6
                draw_table_with_chairs(canvas, 330, 290, 110, 90, {"top": 2, "bottom": 2, "left": 2, "right": 2}, 7)  # Table 7
                draw_table_with_chairs(canvas, 560, 290, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 8)  # Table 8
                draw_table_with_chairs(canvas, 790, 290, 150, 90, {"top": 3, "bottom": 3, "left": 2, "right": 2}, 9)  # Table 9
                draw_table_with_chairs(canvas, 1050, 290, 140, 90, {"top": 3, "bottom": 3, "left": 1, "right": 1}, 10) # Table 10

                # Row 3
                draw_table_with_chairs(canvas, 70, 530, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 11)   # Table 11
                draw_table_with_chairs(canvas, 290, 530, 180, 90, {"top": 4, "bottom": 4, "left": 2, "right": 2}, 12)  # Table 12
                draw_table_with_chairs(canvas, 580, 530, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 13)  # Table 13
                draw_table_with_chairs(canvas, 810, 530, 150, 90, {"top": 3, "bottom": 3, "left": 2, "right": 2}, 14)  # Table 14
                draw_table_with_chairs(canvas, 1080, 530, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 15) # Table 15

            draw_tables()


        # ==========================================

        def SalesMenu():
            SalesFrame = Frame(main_frame, background='darkred')
            SalesFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ==========================================

        def LogoutMenu():
            self.window.destroy()

        # ==========================================































def win():
    window = Tk()
    AdminDashboard(window)
    window.mainloop()

if __name__ == '__main__':

    # loginwindow = Tk()
    # Login(loginwindow)
    # loginwindow.mainloop()
    win()






































