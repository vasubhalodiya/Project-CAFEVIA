def ProductMenu():
            self.AddCoffeeWindow = Tk()
            self.AddCoffeeWindow.title("Add Coffee - CAFEVIA")
            width = 1200
            height = 750
            x = (window.winfo_screenwidth()//2)-(width//2)
            y = (window.winfo_screenheight()//2)-(height//2)
            self.AddCoffeeWindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            self.AddCoffeeWindow.state('normal')
            self.AddCoffeeWindow.resizable(False, False)
            self.AddCoffeeWindow.config(background=secondary_color)

            def Productinsert():
                # ProductId = txtid.get()
                ProductName = self.txtProductName.get()
                ProductCategory = self.txtProductCategory.get()
                ProductAvaliable = self.txtProductAvaliable.get()
                ProductPrice = self.txtProductPrice.get()
                ProductImage = self.txtProductImage.get()

                if(ProductName=="" or ProductCategory=="" or ProductAvaliable=="" or ProductPrice=="" or ProductImage==""):
                    messagebox.showinfo("Insert Status","All fields are required")
                else:
                    con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                    cursor = con.cursor()
                    cursor.execute("insert into product values('"+ProductName+"','"+ProductCategory+"','"+ProductAvaliable+"','"+ProductPrice+"','"+ProductImage+"')")
                    cursor.execute("commit")
                    messagebox.showinfo("INSERT Status","INSERTED SUCCESSFULLY")
                    con.close()

                    # txtid.delete(0,'end')
                    self.txtProductName.delete(0,'end')
                    self.txtProductCategory.delete(0,'end')
                    self.txtProductAvaliable.delete(0,'end')
                    self.txtProductPrice.delete(0,'end')
                    self.txtProductImage.delete(0,'end')
                    messagebox.showinfo("INSERT Status","INSERTED SUCCESSFULLY")
                    con.close()

            def Productinsert():
                ProductName = txtProductName.get()
                ProductCategory = txtProductCategory.get()
                ProductAvaliable = txtProductAvaliable.get()
                ProductPrice = txtProductPrice.get()
                ProductImage = txtProductImage.get()


                if(ProductName=="" or ProductCategory=="" or ProductAvaliable=="" or ProductPrice=="" or ProductImage==""):
                    messagebox.showinfo("Insert Status","All fields are required")
                else:
                    con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                    cursor = con.cursor()
                    cursor.execute("insert into product values('"+ProductName+"','"+ProductCategory+"','"+ProductAvaliable+"','"+ProductPrice+"','"+ProductImage+"')")
                    cursor.execute("commit")
                    messagebox.showinfo("INSERT Status","INSERTED SUCCESSFULLY")
                    con.close()


            self.AddNavbar = Frame(self.AddCoffeeWindow, background=primary_color)
            self.AddNavbar.place(relx=0, rely=0, relwidth=1, relheight=0.5)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Add Coffee", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            self.AddHeadLabel.place(relx=0, rely=0.02, relwidth=1, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Name", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.07, rely=0.1)
            txtProductName = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductName.place(relx=0.07, rely=0.15, relwidth=0.25, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Category", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.07, rely=0.23)
            txtProductCategory = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductCategory.place(relx=0.07, rely=0.28, relwidth=0.25, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Availability", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.07, rely=0.36)
            txtProductAvaliable = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductAvaliable.place(relx=0.07, rely=0.41, relwidth=0.25, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Price", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.4, rely=0.1)
            txtProductPrice = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductPrice.place(relx=0.4, rely=0.15, relwidth=0.25, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Image", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.4, rely=0.23)
            txtProductImage = Entry(self.AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductImage.place(relx=0.4, rely=0.28, relwidth=0.25, relheight=0.05)

            self.AddProductButton = Button(self.AddCoffeeWindow, text="Add Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=Productinsert)
            self.AddProductButton.place(relx=0.73, rely=0.12, relwidth=0.2, relheight=0.08)

            self.EditProductButton = Button(self.AddCoffeeWindow, text= "Edit Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12))
            self.EditProductButton.place(relx=0.73, rely=0.24, relwidth=0.2, relheight=0.08)

            self.DeleteProductButton = Button(self.AddCoffeeWindow, text="Delete Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12))
            self.DeleteProductButton.place(relx=0.73, rely=0.36, relwidth=0.2, relheight=0.08)