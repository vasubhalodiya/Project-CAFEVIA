import MySQLdb
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import io

# Function to fetch and display only product images
def fetch_all_images():
    try:
        # Connect to the database
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()

        # SQL query to fetch all product images
        query = "SELECT proimage FROM product"
        cursor.execute(query)
        results = cursor.fetchall()

        # Clear existing images
        for widget in frame_images.winfo_children():
            widget.destroy()

        # Displaying all product images
        for result in results:
            image_data = result[0]

            # Display image if available
            if image_data:
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((100, 100))  # Resize to fit the label size
                image_tk = ImageTk.PhotoImage(image)

                # Display the image
                img_label = Label(frame_images, image=image_tk)
                img_label.image = image_tk  # Keep a reference to avoid garbage collection
                img_label.pack(side=LEFT, padx=10, pady=10)

        if not results:
            messagebox.showinfo("Info", "No products found.")

    except MySQLdb.OperationalError as e:
        messagebox.showerror("Database Error", f"Operational error: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        con.close()

# Tkinter Setup
root = Tk()
root.title("Fetch All Product Images")

# Frame to hold the images
frame_images = Frame(root)
frame_images.pack()

# Fetch all images automatically when the application starts
fetch_all_images()

# Start the Tkinter main loop
root.mainloop()
