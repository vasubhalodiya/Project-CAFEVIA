def DashboardMenu(root):
    # Frame to hold the Dashboard
    DashboardFrame = Frame(root, background='white')
    DashboardFrame.config(height=620, width=1060)
    DashboardFrame.place(x=0, y=0)

    sidecart_color = "#f5f5f5"
    primary_color = "#333333"
    price_color = "#ffcc00"
    secondary_color = "#ffffff"
    active_color = "#007bff"

    # Create a frame to hold the canvas and scrollbar
    main_frame = Frame(DashboardFrame)
    main_frame.pack(fill="both", expand=True)

    # Add a canvas with a scrollbar
    canvas = Canvas(main_frame)
    scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Create a frame inside the canvas for the product cards
    canvas_frame = Frame(canvas)
    canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

    # Function to dynamically adjust the canvas scrollregion
    def on_canvas_resize(event):
        canvas.config(scrollregion=canvas.bbox("all"))

    canvas_frame.bind("<Configure>", on_canvas_resize)

    # Function to fetch products and display them
    def fetch_products():
        try:
            # Connect to the database
            con = MySQLdb.connect(host="localhost", user="root", password="", database="bookmyshow")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM movie_details")
            products = cursor.fetchall()
            con.close()

            # Clear the existing cards
            for widget in canvas_frame.winfo_children():
                widget.destroy()

            # Display each product in a new card
            row_frame = None
            card_count = 0
            for product in products:
                if card_count % 3 == 0:
                    row_frame = Frame(canvas_frame)
                    row_frame.pack(pady=10)

                ProductCard = Frame(row_frame, background=sidecart_color, bd=1, relief="solid", width=300, height=200)
                ProductCard.grid(row=0, column=card_count % 3, padx=10)

                # Image
                image_path = product[4]  # Assuming product[4] contains the image path
                try:
                    img = Image.open(image_path)
                    img = img.resize((100, 100))
                    photo = ImageTk.PhotoImage(img)
                    ProductImageLabel = Label(ProductCard, image=photo, bg=sidecart_color)
                    ProductImageLabel.image = photo  # Keep reference to avoid garbage collection
                    ProductImageLabel.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.4)
                except Exception as e:
                    print(f"Error loading image: {e}")

                # Category
                ProductCategoryLabel = Label(ProductCard, text=product[2], bg=sidecart_color, fg=primary_color,
                                             font=("century gothic", 8))
                ProductCategoryLabel.place(relx=0, rely=0.56, relwidth=0.32, relheight=0.09)

                # Product Name
                ProductNameLabel = Label(ProductCard, text=product[1], bg=sidecart_color, fg=primary_color,
                                         font=("century gothic bold", 13), anchor="w")
                ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)

                # Price
                ProductPriceLabel = Label(ProductCard, text=f"₹ {product[3]}", bg=price_color, fg=sidecart_color,
                                           font=("century gothic bold", 15))
                ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)

                # Add to Cart Button
                ProductAddToCardButton = Button(ProductCard, text="Add", font=("century gothic bold", 11), width=27,
                                                height=1, background=primary_color, foreground=secondary_color,
                                                cursor="hand2", relief="flat", activebackground=active_color, bd=2)
                ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)

                card_count += 1

            # Update the scrollregion to fit all the cards
            canvas.config(scrollregion=canvas.bbox("all"))

        except MySQLdb.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    # Call the fetch_products function
    fetch_products()