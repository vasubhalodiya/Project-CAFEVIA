import MySQLdb
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import io

# Function to fetch product details (including image) and display it
def fetch_and_display_image():
    proid = txtProductID.get()  # Assuming there's a text field for the product ID
    
    if not proid:
        messagebox.showinfo("Error", "Product ID is required to fetch image.")
        return

    try:
        # Connect to the database
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()

        # SQL query to fetch product details and image
        query = "SELECT proimage FROM product WHERE proid = %s"
        cursor.execute(query, (proid,))
        result = cursor.fetchone()

        if result:
            # Extracting the data from the result tuple
            image_data = result

            # If image data exists, convert it and display
            if image_data:
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((200, 200))  # Resize to fit the label size
                image_tk = ImageTk.PhotoImage(image)

                # If an image is already displayed, update it
                lblProductImage.config(image=image_tk)
                lblProductImage.image = image_tk  # Keep a reference to avoid garbage collection
            else:
                lblProductImage.config(image=None)
                lblProductImage.image = None

        else:
            messagebox.showinfo("Error", "Product not found.")

    except MySQLdb.OperationalError as e:
        messagebox.showerror("Database Error", f"Operational error: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        con.close()

# Tkinter Setup
root = Tk()
root.title("Fetch Product Image")

# Product ID input
Label(root, text="Enter Product ID:").grid(row=0, column=0, padx=10, pady=10)
txtProductID = Entry(root)
txtProductID.grid(row=0, column=1, padx=10, pady=10)

# Buttons and Labels for displaying product details
btnFetchImage = Button(root, text="Fetch Image", command=fetch_and_display_image)
btnFetchImage.grid(row=1, column=0, columnspan=2, pady=10)

lblProductImage = Label(root)
lblProductImage.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
