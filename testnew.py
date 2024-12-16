import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3
import io

# Connect to the cafevia database
conn = sqlite3.connect("cafevia.db")
cursor = conn.cursor()

# Ensure the product table exists (modify as needed)
cursor.execute("""
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    proimage BLOB
)
""")
conn.commit()

# Function to insert an image into the product table
def insert_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_path:
        try:
            with open(file_path, "rb") as file:
                img_blob = file.read()
            # Insert image as binary data into the product table
            cursor.execute("INSERT INTO product (name, proimage) VALUES (?, ?)", 
                           (file_path, img_blob))
            conn.commit()
            messagebox.showinfo("Success", "Image inserted into the product table!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to insert image: {e}")

# Function to fetch and display the last inserted image
def fetch_image():
    cursor.execute("SELECT proimage FROM product ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        try:
            img_blob = row[0]
            # Convert binary data to image
            img = Image.open(io.BytesIO(img_blob))
            img.thumbnail((400, 400))  # Resize for display
            img_tk = ImageTk.PhotoImage(img)
            # Display the image
            image_label.config(image=img_tk)
            image_label.image = img_tk
            image_label.text = ""
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display image: {e}")
    else:
        messagebox.showinfo("No Image", "No images found in the product table!")

# Create the main application window
root = tk.Tk()
root.title("Image Upload and Fetch for Cafevia")

# Add buttons for uploading and fetching images
upload_button = tk.Button(root, text="Upload Image", command=insert_image)
upload_button.pack(pady=10)

fetch_button = tk.Button(root, text="Fetch Last Image", command=fetch_image)
fetch_button.pack(pady=10)

# Add a label to display the image
image_label = tk.Label(root, text="No image uploaded", bg="lightgrey", width=50, height=20)
image_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

# Close the database connection when done
conn.close()
