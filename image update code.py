def ProductUpdate():
    global selected_file_path  # To access the file path of the selected image

    ProductId = txtProductId.get()
    ProductName = txtProductName.get()
    ProductCategory = txtProductCategory.get()
    ProductAvaliable = txtProductAvaliable.get()
    ProductPrice = txtProductPrice.get()

    # Validation
    if ProductId == "" or ProductName == "" or ProductCategory == "" or ProductAvaliable == "" or ProductPrice == "":
        messagebox.showinfo("Update Status", "All fields except image are required")
        return

    image_data = None
    if selected_file_path:  # Check if a new image is selected
        try:
            with open(selected_file_path, "rb") as file:
                image_data = file.read()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read image file: {str(e)}")
            return

    try:
        # Connect to the database
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()

        # SQL query to update the product
        if image_data:
            query = """UPDATE product 
                       SET proname=%s, procategory=%s, proavailable=%s, proprice=%s, proimage=%s 
                       WHERE proid=%s"""
            values = (ProductName, ProductCategory, ProductAvaliable, ProductPrice, image_data, ProductId)
        else:
            query = """UPDATE product 
                       SET proname=%s, procategory=%s, proavailable=%s, proprice=%s 
                       WHERE proid=%s"""
            values = (ProductName, ProductCategory, ProductAvaliable, ProductPrice, ProductId)

        cursor.execute(query, values)
        con.commit()

        # Clear input fields and reset the selected image
        txtProductId.delete(0, 'end')
        txtProductName.delete(0, 'end')
        txtProductCategory.delete(0, 'end')
        txtProductAvaliable.delete(0, 'end')
        txtProductPrice.delete(0, 'end')
        selected_file_path = None  # Reset the image path
        if 'image_preview' in globals():
            image_preview.config(image='')  # Clear the preview if it exists

        messagebox.showinfo("UPDATE Status", "UPDATED SUCCESSFULLY")

    except MySQLdb.OperationalError as e:
        messagebox.showerror("Database Error", f"Operational error: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        con.close()
