import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
from PIL import Image, ImageTk

# MySQL Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="", 
        database="productdb"
    )

# Function to insert product data into the database
def insert_product():
    product_name = entry_name.get()
    price = entry_price.get()
    image_path = label_image_path.cget("text")

    if not product_name or not price or image_path == "No image selected":
        messagebox.showerror("Input Error", "All fields are required!")
        return
    
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "INSERT INTO products (product_name, price, image_path) VALUES (%s, %s, %s)"
        cursor.execute(query, (product_name, price, image_path))
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Success", "Product added successfully!")
        clear_form()

        # Immediately show the product card after submission
        fetch_products()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Function to browse and select an image
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        label_image_path.config(text=file_path)
        display_image(file_path)

# Function to display image in the Tkinter window
def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((100, 100))
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

# Function to fetch and display products from the database
def fetch_products():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        cursor.close()
        connection.close()

        # Clear previous product cards
        for widget in frame_products.winfo_children():
            widget.destroy()

        # Create new product cards with a limit of 3 cards per row
        row_frame = None
        card_count = 0

        for product in products:
            if card_count % 3 == 0:  # Create a new row after every 3 cards
                row_frame = tk.Frame(frame_products)
                row_frame.pack(pady=10)

            product_card = tk.Frame(row_frame, bd=1, relief="solid", width=300, height=400, bg="red", padx=10, pady=10)
            product_card.grid(row=0, column=card_count % 3, padx=10)

            img_path = product[3]
            img = Image.open(img_path)
            img = img.resize((200, 200))
            img = ImageTk.PhotoImage(img)

            img_label = tk.Label(product_card, image=img, bg="red")
            img_label.image = img
            img_label.place(x=50, y=10)

            tk.Label(product_card, text=product[1], font=("Helvetica", 12, "bold"), fg="black", bg="red").place(x=50, y=220)
            tk.Label(product_card, text=f"${product[2]}", font=("Helvetica", 10), fg="black", bg="red").place(x=50, y=250)

            card_count += 1

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Function to clear the form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    label_image_path.config(text="No image selected")
    panel.config(image="")

# Tkinter GUI
root = tk.Tk()
root.title("Product Form")

# Create the form elements
tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Price:").grid(row=1, column=0, padx=10, pady=10)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Product Image:").grid(row=2, column=0, padx=10, pady=10)
label_image_path = tk.Label(root, text="No image selected", fg="blue")
label_image_path.grid(row=2, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse Image", command=browse_image)
browse_button.grid(row=2, column=2, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=insert_product)
submit_button.grid(row=3, column=1, pady=20)

# Product display section
tk.Label(root, text="Products").grid(row=4, column=0, columnspan=3, pady=10)

frame_products = tk.Frame(root)
frame_products.grid(row=5, column=0, columnspan=3, pady=10)

# Panel to display selected image
panel = tk.Label(root)
panel.grid(row=3, column=2, rowspan=2, padx=10, pady=10)

# Fetch and display products on startup
fetch_products()

# Run the Tkinter main loop
root.mainloop()
