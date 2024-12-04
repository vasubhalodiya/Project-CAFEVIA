if not all([ProductName, ProductCategory, ProductAvaliable, ProductPrice, ProductImage]):
    messagebox.showinfo("Insert Status", "All fields are required")
    return

try:
    con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
    cursor = con.cursor()
    query = "INSERT INTO product (proname, procategory, proavailable, proprice, proimage) VALUES (%s, %s, %s, %s, %s)"
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