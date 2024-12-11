ProductCard = Frame(CoffeeCategory, background=sidecart_color)
ProductCard.place(relx=0.27, rely=0.08, relwidth=0.21, relheight=0.25)
# *********************
ProductCardImage = Image.open('images/coffee.png').resize((75, 75))
ProductCardImage = ImageTk.PhotoImage(ProductCardImage)
ProductCardImage_label = Label(ProductCard, image=ProductCardImage, background=sidecart_color)
ProductCardImage_label.image = ProductCardImage
ProductCardImage_label.place(relx=0.3, rely=0.08, width=75, height=75)
# *********************
ProductCategoryLabel = Label(ProductCard, text="Coffee", bg=sidecart_color, fg=primary_color, font=("century gothic", 8))
ProductCategoryLabel.place(relx=0, rely=0.56, relwidth=0.32, relheight=0.09)
# *********************
ProductNameLabel = Label(ProductCard, text="Hello World Coffee", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13), anchor="w") # wraplength=180
ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)
# *********************
ProductAddToCardButton = Button(ProductCard, text="Add", font=("century gothic bold", 11), width=27, height=1, background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)
# *********************
ProductPriceLabel = Label(ProductCard, text="₹ 100", bg=price_color, fg=sidecart_color, font=("century gothic bold", 15))
ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)