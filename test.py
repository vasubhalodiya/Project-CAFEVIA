from tkinter import Tk, Frame, Label, Button, Canvas, Scrollbar
from PIL import Image, ImageTk
import MySQLdb
import os

# Colors for the UI
top_color = "#f8f9fa"
secondary_color = "#ffffff"
sidecart_color = "#e9ecef"
primary_color = "#007bff"
price_color = "#ffc107"
active_color = "#0056b3"

# Create main window
root = Tk()
root.title("Cafecia Product Display")
root.geometry("800x600")

# Canvas for scrolling
canvas = Canvas(root, bg=top_color)
canvas.pack(side="left", fill="both", expand=True)

# Scrollbar for the canvas
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Frame inside the canvas
canvas_frame = Frame(canvas, bg=top_color)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Database and card creation
try:
    # Connect to the database
    con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    con.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")
    products = []

row_frame = None
card_count = 0
for product_details in products:
    if card_count % 4 == 0:
        row_frame = Frame(canvas_frame, background=secondary_color)
        row_frame.pack(padx=20, pady=10)

    ProductDtlCard = Frame(row_frame, background=sidecart_color, width=200, height=210)
    ProductDtlCard.grid(row=0, column=card_count % 4, padx=15)

    # Image
    try:
        img_path = product_details[5]  # Assuming the 6th column is the image path
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((160, 120))  # Resize to fit the card
            tk_img = ImageTk.PhotoImage(img)

            ProductImageLabel = Label(ProductDtlCard, image=tk_img, bg=sidecart_color)
            ProductImageLabel.image = tk_img  # Keep a reference to avoid garbage collection
            ProductImageLabel.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.45)
        else:
            raise FileNotFoundError(f"Image file does not exist: {img_path}")
    except Exception as e:
        print(f"Error loading image for product {product_details[1]}: {e}")
        PlaceholderLabel = Label(ProductDtlCard, text="No Image", bg=sidecart_color, fg="gray")
        PlaceholderLabel.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.45)

    # Category
    ProductCategoryLabel = Label(ProductDtlCard, text=product_details[3], bg=sidecart_color, fg=primary_color, font=("century gothic", 8), anchor="w")
    ProductCategoryLabel.place(relx=0.05, rely=0.56, relwidth=0.32, relheight=0.09)

    # Product Name
    ProductNameLabel = Label(ProductDtlCard, text=product_details[2], bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13), anchor="w")
    ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)

    # Price
    ProductPriceLabel = Label(ProductDtlCard, text=f"\u20B9 {product_details[4]}", bg=price_color, fg=sidecart_color, font=("century gothic bold", 15))
    ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)

    # Add to Cart Button
    ProductAddToCardButton = Button(ProductDtlCard, text="Add", font=("century gothic bold", 11), width=27, height=1, background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
    ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)

    card_count += 1

# Update canvas scroll region
def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas_frame.bind("<Configure>", update_scroll_region)

# Start the Tkinter event loop
root.mainloop()
