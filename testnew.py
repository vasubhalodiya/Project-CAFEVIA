import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import MySQLdb

primary_color = "#6A1B9A"  # Replace with your color values
secondary_color = "#F3E5F5"
sidecart_color = "#FFFFFF"
active_color = "#9C27B0"
price_color = "#FFEB3B"


# Function to insert product into the database
def Productinsert():
    ProductName = txtProductName.get()
    ProductCategory = txtProductCategory.get()
    ProductAvaliable = txtProductAvaliable.get()
    ProductPrice = txtProductPrice.get()
    ProductImage = txtProductImage.get()

    if(ProductName == "" or ProductCategory == "" or ProductAvaliable == "" or ProductPrice == "" or ProductImage == ""):
        messagebox.showinfo("Insert Status", "All fields are required")
    else:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()
        cursor.execute("INSERT INTO product (proname, procategory, proavailable, proprice, proimage) VALUES (%s, %s, %s, %s, %s)", (ProductName, ProductCategory, ProductAvaliable, ProductPrice, ProductImage))
        con.commit()
        con.close()
        messagebox.showinfo("INSERT Status", "INSERTED SUCCESSFULLY")
        fetch_products()  # Fetch products to update the product cards

# Function to fetch products from the database and display them in product cards
def fetch_products():
    con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    con.close()

    # Clear the existing cards (if any)
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    # Display each product in a new card
    row_frame = None
    card_count = 0
    for product in products:
        if card_count % 3 == 0:  # Create a new row for every 3 cards
            row_frame = tk.Frame(canvas_frame)
            row_frame.pack(pady=10)

        ProductCard = tk.Frame(row_frame, background=sidecart_color, bd=1, relief="solid", width=300, height=200)
        ProductCard.grid(row=0, column=card_count % 3, padx=10)

        # Image
        

        # Category
        ProductCategoryLabel = tk.Label(ProductCard, text=product[2], bg=sidecart_color, fg=primary_color, font=("century gothic", 8))
        ProductCategoryLabel.place(relx=0, rely=0.56, relwidth=0.32, relheight=0.09)

        # Product Name
        ProductNameLabel = tk.Label(ProductCard, text=product[1], bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13), anchor="w")
        ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)

        # Price
        ProductPriceLabel = tk.Label(ProductCard, text=f"₹ {product[3]}", bg=price_color, fg=sidecart_color, font=("century gothic bold", 15))
        ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)

        # Add to Cart Button
        ProductAddToCardButton = tk.Button(ProductCard, text="Add", font=("century gothic bold", 11), width=27, height=1, background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
        ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)

        card_count += 1

    # After adding cards, update the scrollregion to fit all the cards
    canvas.config(scrollregion=canvas.bbox("all"))

# Tkinter GUI Setup
root = tk.Tk()
root.title("Product Management - CAFEVIA")
width = 1200
height = 750
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(False, False)
root.config(background=secondary_color)

# Navbar
AddNavbar = tk.Frame(root, background=primary_color)
AddNavbar.place(relx=0, rely=0, relwidth=1, relheight=0.5)

# Title Label
AddHeadLabel = tk.Label(root, text="Add Product", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
AddHeadLabel.place(relx=0, rely=0.02, relwidth=1, relheight=0.05)

# Form fields (Product ID, Category, etc.)
txtProductId = tk.Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
txtProductId.place(relx=0.07, rely=0.15, relwidth=0.25, relheight=0.05)

txtProductCategory = tk.Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
txtProductCategory.place(relx=0.07, rely=0.28, relwidth=0.25, relheight=0.05)

txtProductAvaliable = tk.Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
txtProductAvaliable.place(relx=0.07, rely=0.41, relwidth=0.25, relheight=0.05)

txtProductName = tk.Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
txtProductName.place(relx=0.4, rely=0.15, relwidth=0.25, relheight=0.05)

txtProductPrice = tk.Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
txtProductPrice.place(relx=0.4, rely=0.28, relwidth=0.25, relheight=0.05)

txtProductImage = tk.Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
txtProductImage.place(relx=0.4, rely=0.41, relwidth=0.25, relheight=0.05)

# Add Product Button
AddProductButton = tk.Button(root, text="Add Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=Productinsert)
AddProductButton.place(relx=0.73, rely=0.12, relwidth=0.2, relheight=0.08)

# Create a canvas for scrolling
canvas = tk.Canvas(root)
canvas.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# Create a vertical scrollbar linked to the canvas
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.place(relx=0.97, rely=0.5, relwidth=0.03, relheight=0.5)

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the product cards
canvas_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Fetch and display products on startup
fetch_products()

root.mainloop()
