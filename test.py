import MySQLdb
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import io

# Colors
primary_color = "#3f9e4f"
secondary_color = "#ffffff"
sidecart_color = "#d3d3d3"
active_color = "#2d8b43"
price_color = "#ffbf00"

# Global variable to hold the selected image path
selected_image_path = None


def browse_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(
        title="Select Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")]
    )
    if selected_image_path:
        # Preview the selected image
        img = Image.open(selected_image_path)
        img = img.resize((100, 100), Image.ANTIALIAS)  # Resize image for preview
        img_preview = ImageTk.PhotoImage(img)
        lblImagePreview.configure(image=img_preview)
        lblImagePreview.image = img_preview  # Save reference to avoid garbage collection


def Productinsert():
    global selected_image_path
    ProductName = txtProductName.get()
    ProductCategory = txtProductCategory.get()
    ProductAvaliable = txtProductAvaliable.get()
    ProductPrice = txtProductPrice.get()

    if not all([ProductName, ProductCategory, ProductAvaliable, ProductPrice, selected_image_path]):
        messagebox.showinfo("Insert Status", "All fields are required")
        return

    try:
        # Read the image as binary data
        with open(selected_image_path, "rb") as img_file:
            binary_image = img_file.read()

        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()
        query = """
            INSERT INTO product (proname, procategory, proavailable, proprice, proimage)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (ProductName, ProductCategory, ProductAvaliable, ProductPrice, binary_image))
        con.commit()

        txtProductName.delete(0, "end")
        txtProductCategory.delete(0, "end")
        txtProductAvaliable.delete(0, "end")
        txtProductPrice.delete(0, "end")
        lblImagePreview.configure(image="")
        selected_image_path = None

        messagebox.showinfo("Insert Status", "Inserted Successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        con.close()


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


# Main window
AddCoffeeWindow = Tk()
AddCoffeeWindow.title("Add Coffee - CAFEVIA")
width = 1200
height = 750
x = (AddCoffeeWindow.winfo_screenwidth() // 2) - (width // 2)
y = (AddCoffeeWindow.winfo_screenheight() // 2) - (height // 2)
AddCoffeeWindow.geometry(f'{width}x{height}+{x}+{y}')
AddCoffeeWindow.resizable(False, False)
AddCoffeeWindow.config(background=secondary_color)

# Navbar (top)
AddNavbar = Frame(AddCoffeeWindow, background=primary_color)
AddNavbar.place(relx=0, rely=0, relwidth=1, relheight=0.5)

AddHeadLabel = Label(AddCoffeeWindow, text="Add Coffee", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
AddHeadLabel.place(relx=0, rely=0.02, relwidth=1, relheight=0.05)

# Product Fields
lblProductName = Label(AddCoffeeWindow, text="Product Name", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
lblProductName.place(relx=0.07, rely=0.1)
txtProductName = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
txtProductName.place(relx=0.07, rely=0.15, relwidth=0.25, relheight=0.05)

lblProductCategory = Label(AddCoffeeWindow, text="Product Category", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
lblProductCategory.place(relx=0.07, rely=0.23)
txtProductCategory = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
txtProductCategory.place(relx=0.07, rely=0.28, relwidth=0.25, relheight=0.05)

lblProductAvaliable = Label(AddCoffeeWindow, text="Product Availability", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
lblProductAvaliable.place(relx=0.07, rely=0.36)
txtProductAvaliable = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
txtProductAvaliable.place(relx=0.07, rely=0.41, relwidth=0.25, relheight=0.05)

lblProductPrice = Label(AddCoffeeWindow, text="Product Price", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
lblProductPrice.place(relx=0.4, rely=0.1)
txtProductPrice = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
txtProductPrice.place(relx=0.4, rely=0.15, relwidth=0.25, relheight=0.05)

# Image Selection and Preview
lblProductImage = Label(AddCoffeeWindow, text="Product Image", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
lblProductImage.place(relx=0.4, rely=0.36)

btnBrowseImage = Button(AddCoffeeWindow, text="Browse Image", command=browse_image, font=("century gothic bold", 12), background=secondary_color, foreground=primary_color, relief="flat")
btnBrowseImage.place(relx=0.4, rely=0.41, relwidth=0.25, relheight=0.05)

lblImagePreview = Label(AddCoffeeWindow, bg=secondary_color)
lblImagePreview.place(relx=0.68, rely=0.41, width=100, height=100)

# Add Product Button
AddProductButton = Button(AddCoffeeWindow, text="Add Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=Productinsert)
AddProductButton.place(relx=0.73, rely=0.12, relwidth=0.2, relheight=0.08)

# Data Grid (Treeview for fetched products)
CRUDtxtDatagridView = Frame(AddCoffeeWindow, background=secondary_color)
CRUDtxtDatagridView.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# Treeview for displaying products
my_tree = ttk.Treeview(CRUDtxtDatagridView)
my_tree['columns'] = ("proid", "proimage", "proname", "procategory", "proprice", "proavaliable")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("proid", anchor="w", width=100)
my_tree.column("proimage", anchor="w", width=220)
my_tree.column("proname", anchor="w", width=220)
my_tree.column("procategory", anchor="w", width=220)
my_tree.column("proprice", anchor="w", width=220)
my_tree.column("proavaliable", anchor="w", width=220)

my_tree.heading("#0", text="Label", anchor="w")
my_tree.heading("proid", text="Product Id", anchor="w")
my_tree.heading("proimage", text="Product Image", anchor="w")
my_tree.heading("proname", text="Product Name", anchor="w")
my_tree.heading("procategory", text="Product Category", anchor="w")
my_tree.heading("proprice", text="Product Price", anchor="w")
my_tree.heading("proavaliable", text="Product Available", anchor="w")

my_tree.pack()
fetch_data()

AddCoffeeWindow.mainloop()
