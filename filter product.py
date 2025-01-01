import tkinter as tk
from tkinter import Label, Button, Frame, Canvas, Scrollbar
from PIL import Image, ImageTk
import MySQLdb
import mysql.connector
import io

# Colors (define these values as per your theme)
primary_color = "#000000"
secondary_color = "#FFFFFF"
sidecart_color = "#F5F5F5"
active_color = "#E0E0E0"
price_color = "#FF5733"

# Sample categories
categories = [
    {"name": "All", "image": "images/all.png"},
    {"name": "Coffee", "image": "images/coffee.png"},
    {"name": "Softdrink", "image": "images/softdrink.png"},
    {"name": "Pizza", "image": "images/pizza.png"},
    {"name": "Burger", "image": "images/burger.png"},
    {"name": "Dessert", "image": "images/dessert.png"},
    {"name": "Food Meal", "image": "images/meal.png"},
]

# Create the main window
root = tk.Tk()
root.title("Cafe Menu")
root.geometry("900x700")

# Main Frame
MenuFrame = Frame(root, bg=secondary_color)
MenuFrame.pack(fill="both", expand=True)

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

        # Fetch and display the image for the current product
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

        cursor.execute("SELECT cartqty, cartprice FROM cart WHERE cartname = %s", (product_name,))
        cart_item = cursor.fetchone()

        if cart_item:
            new_qty = cart_item[0] + 1
            new_total = new_qty * product_price
            cursor.execute("UPDATE cart SET cartqty = %s WHERE cartname = %s", 
                        (new_qty, new_total, product_name))
        else:
            cart_total = product_price
            cursor.execute("INSERT INTO cart (cartname, cartqty, cartprice) VALUES (%s, %s, %s)", 
                        (product_name, 1, product_price))

        con.commit()
        print(f"Added {product_name} to cart successfully!")
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
AddProductButton = Button(CoffeeCategory, text="Add Product", background=primary_color, foreground=secondary_color, cursor="hand2", relief="solid", activebackground=active_color, bd=0, font=("century gothic bold", 12))
AddProductButton.place(relx=0.815, rely=0.02, relwidth=0.15, relheight=0.05)

# Add a scrollbar to the ProductCategorymain_frame
ProductCategorymain_frame = Frame(CoffeeCategory)
ProductCategorymain_frame.place(relx=0, rely=0.08, relwidth=1, relheight=0.66)

# Create a Canvas inside the ProductCategorymain_frame
Produc_canvas = Canvas(ProductCategorymain_frame, bg=secondary_color, bd=0, highlightthickness=0)
Produc_canvas.pack(side="left", fill="both", expand=True)

# Create a vertical scrollbar
scrollbar = Scrollbar(ProductCategorymain_frame, orient="vertical", command=Produc_canvas.yview)
scrollbar.place(relx=0.988, rely=0, relwidth=0.013, relheight=1)

# Configure the canvas to use the scrollbar
Produc_canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the content
canvas_frame = Frame(Produc_canvas, background=secondary_color)
Produc_canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Bind the canvas to resize the scroll region
def update_scrollregion(event):
    Produc_canvas.configure(scrollregion=Produc_canvas.bbox("all"))

canvas_frame.bind("<Configure>", update_scrollregion)

# Add mousewheel scrolling functionality
def on_mousewheel(event):
    Produc_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

Produc_canvas.bind_all("<MouseWheel>", on_mousewheel)

# Initially display products from "All" category after canvas_frame is created
filter_products_by_category("All")

# Run the application
root.mainloop()
