# Function to fetch image for each product by product ID
def fetch_image(product_id):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="cafevia")
    cursor = con.cursor()
    cursor.execute("SELECT image_column FROM product WHERE product_id = %s", (product_id,))  # Replace `image_column` with the actual column name
    image_data = cursor.fetchone()
    con.close()

    if image_data:
        # Convert BLOB data to an image
        img = Image.open(io.BytesIO(image_data[0]))  # Assuming image is the first column
        img = img.resize((150, 150))  # Resize image as needed
        return ImageTk.PhotoImage(img)
    return None

row_frame = None
card_count = 0
for product_details in products:
    if card_count % 4 == 0:
        row_frame = Frame(canvas_frame, background=secondary_color)
        row_frame.pack(padx=20, pady=10)

    ProductDtlCard = Frame(row_frame, background=sidecart_color, width=200, height=210)
    ProductDtlCard.grid(row=0, column=card_count % 4, padx=15)

    # Fetch and display the image for the current product
    product_id = product_details[0]  # Assuming the product ID is in the first column (index 0)
    product_image = fetch_image(product_id)
    if product_image:
        # Display image in a label
        label = tk.Label(ProductDtlCard, image=product_image)
        label.image = product_image  # Keep reference to avoid garbage collection
        label.pack(pady=10)

    # Category
    ProductCategoryLabel = Label(ProductDtlCard, text=product_details[3], bg=sidecart_color, fg=primary_color, font=("century gothic", 8), anchor="w")
    ProductCategoryLabel.place(relx=0.05, rely=0.56, relwidth=0.32, relheight=0.09)

    # Product Name
    ProductNameLabel = Label(ProductDtlCard, text=product_details[2], bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13), anchor="w")
    ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)

    # Price
    ProductPriceLabel = Label(ProductDtlCard, text=f"₹ {product_details[4]}", bg=price_color, fg=sidecart_color, font=("century gothic bold", 15))
    ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)

    # Add to Cart Button
    ProductAddToCardButton = Button(ProductDtlCard, text="Add", font=("century gothic bold", 11), width=27, height=1, background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
    ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)

    card_count += 1
