import MySQLdb
from tkinter import Tk, Frame, Label, Entry, Button, messagebox

primary_color = "#1a1a1a"
secondary_color = "#f0f0f0"
active_color = "#cccccc"

def ProductMenu():
    self.AddCoffeeWindow = Tk()
    self.AddCoffeeWindow.title("Add Coffee - CAFEVIA")
    width = 1200
    height = 750
    x = (self.AddCoffeeWindow.winfo_screenwidth() // 2) - (width // 2)
    y = (self.AddCoffeeWindow.winfo_screenheight() // 2) - (height // 2)
    self.AddCoffeeWindow.geometry(f'{width}x{height}+{x}+{y}')
    self.AddCoffeeWindow.resizable(False, False)
    self.AddCoffeeWindow.config(background=secondary_color)

    def Productinsert():
        ProductName = self.txtProductName.get()
        ProductCategory = self.txtProductCategory.get()
        ProductAvaliable = self.txtProductAvaliable.get()
        ProductPrice = self.txtProductPrice.get()
        ProductImage = self.txtProductImage.get()

        if not all([ProductName, ProductCategory, ProductAvaliable, ProductPrice, ProductImage]):
            messagebox.showinfo("Insert Status", "All fields are required")
            return

        try:
            con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
            cursor = con.cursor()

            query = "INSERT INTO product (ProductName, ProductCategory, ProductAvaliable, ProductPrice, ProductImage) VALUES (%s, %s, %s, %s, %s)"
            values = (ProductName, ProductCategory, ProductAvaliable, ProductPrice, ProductImage)

            cursor.execute(query, values)
            con.commit()

            messagebox.showinfo("INSERT Status", "Inserted Successfully")

            # Clear fields after insertion
            self.txtProductName.delete(0, 'end')
            self.txtProductCategory.delete(0, 'end')
            self.txtProductAvaliable.delete(0, 'end')
            self.txtProductPrice.delete(0, 'end')
            self.txtProductImage.delete(0, 'end')
        except MySQLdb.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            if con:
                con.close()

    # UI elements
    self.AddNavbar = Frame(self.AddCoffeeWindow, background=primary_color)
    self.AddNavbar.place(relx=0, rely=0, relwidth=1, relheight=0.5)

    self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Add Coffee", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
    self.AddHeadLabel.place(relx=0, rely=0.02, relwidth=1, relheight=0.05)

    self.txtProductName = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
    self.txtProductName.place(relx=0.07, rely=0.15, relwidth=0.25, relheight=0.05)

    self.txtProductCategory = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
    self.txtProductCategory.place(relx=0.07, rely=0.28, relwidth=0.25, relheight=0.05)

    self.txtProductAvaliable = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
    self.txtProductAvaliable.place(relx=0.07, rely=0.41, relwidth=0.25, relheight=0.05)

    self.txtProductPrice = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
    self.txtProductPrice.place(relx=0.4, rely=0.15, relwidth=0.25, relheight=0.05)

    self.txtProductImage = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
    self.txtProductImage.place(relx=0.4, rely=0.28, relwidth=0.25, relheight=0.05)

    self.AddProductButton = Button(self.AddCoffeeWindow, text="Add Product", background=secondary_color, foreground=primary_color,
                                   cursor="hand2", relief="flat", activebackground=active_color, bd=2,
                                   font=("century gothic bold", 12), command=Productinsert)
    self.AddProductButton.place(relx=0.73, rely=0.12, relwidth=0.2, relheight=0.08)

    self.AddCoffeeWindow.mainloop()
