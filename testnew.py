import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import MySQLdb

# Connect to MySQL database
conn = MySQLdb.connect(
    host="localhost",
    user="root",
    password="",
    database="try"
)
cursor = conn.cursor()

def insert_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
    if not filepath:
        return

    name = name_entry.get()
    if not name:
        messagebox.showerror("Error", "Please enter a name for the image.")
        return

    with open(filepath, "rb") as file:
        binary_data = file.read()

    query = "INSERT INTO try_data_table (name, image) VALUES (%s, %s)"
    cursor.execute(query, (name, binary_data))
    conn.commit()
    messagebox.showinfo("Success", "Image inserted successfully.")
    fetch_images()

def update_image():
    selected_id = get_selected_id()
    if not selected_id:
        return

    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
    if not filepath:
        return

    with open(filepath, "rb") as file:
        binary_data = file.read()

    query = "UPDATE try_data_table SET image = %s WHERE id = %s"
    cursor.execute(query, (binary_data, selected_id))
    conn.commit()
    messagebox.showinfo("Success", "Image updated successfully.")
    fetch_images()

def delete_image():
    selected_id = get_selected_id()
    if not selected_id:
        return

    query = "DELETE FROM try_data_table WHERE id = %s"
    cursor.execute(query, (selected_id,))
    conn.commit()
    messagebox.showinfo("Success", "Image deleted successfully.")
    fetch_images()

def fetch_images():
    query = "SELECT id, name FROM try_data_table"
    cursor.execute(query)
    rows = cursor.fetchall()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")

def get_selected_id():
    selection = listbox.curselection()
    if not selection:
        messagebox.showerror("Error", "Please select an image from the list.")
        return None

    selected_item = listbox.get(selection[0])
    return int(selected_item.split(" - ")[0])

def show_image():
    selected_id = get_selected_id()
    if not selected_id:
        return

    query = "SELECT image FROM try_data_table WHERE id = %s"
    cursor.execute(query, (selected_id,))
    row = cursor.fetchone()
    if not row:
        messagebox.showerror("Error", "Image not found.")
        return

    binary_data = row[0]
    with open("temp_image.png", "wb") as file:
        file.write(binary_data)

    img = Image.open("temp_image.png")
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

# GUI Setup
root = tk.Tk()
root.title("Image Management with MySQL")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

insert_btn = tk.Button(frame, text="Insert", command=insert_image)
insert_btn.grid(row=0, column=2, padx=5, pady=5)

update_btn = tk.Button(frame, text="Update", command=update_image)
update_btn.grid(row=0, column=3, padx=5, pady=5)

delete_btn = tk.Button(frame, text="Delete", command=delete_image)
delete_btn.grid(row=0, column=4, padx=5, pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

fetch_btn = tk.Button(root, text="Fetch Images", command=fetch_images)
fetch_btn.pack(pady=5)
0
show_btn = tk.Button(root, text="Show Image", command=show_image)
show_btn.pack(pady=5)

image_label = tk.Label(root)
image_label.pack(pady=10)

fetch_images()
root.mainloop()

# Close database connection on exit
conn.close()
