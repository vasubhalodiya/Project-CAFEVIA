import MySQLdb
from tkinter import Tk, Label, Button, Entry, filedialog
from PIL import Image, ImageTk

# Database connection
con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
cursor = con.cursor()

def insert_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png")])
    if path:
        with open(path, 'rb') as file:
            cursor.execute("UPDATE product SET proimage = %s WHERE proid = %s", (file.read(), entry_id.get()))
        con.commit()

def fetch_image():
    cursor.execute("SELECT proimage FROM product WHERE proid = %s", (entry_id.get(),))
    data = cursor.fetchone()
    if data and data[0]:
        img = ImageTk.PhotoImage(Image.open(io.BytesIO(data[0])).resize((200, 200)))
        label_img.config(image=img)
        label_img.image = img

root = Tk()
entry_id = Entry(root); entry_id.pack()
Button(root, text="Insert Image", command=insert_image).pack()
Button(root, text="Fetch Image", command=fetch_image).pack()
label_img = Label(root); label_img.pack()
root.mainloop()
