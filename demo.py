import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")

# Functionality for menu system
main_frame = Frame(window, background='#E7E0D6')
main_frame.place(relx=0.18, rely=0, relwidth=0.82, relheight=1)
OrderFrame = Frame(main_frame, background='#E7E0D6')
OrderFrame.place(relx=0, rely=0, relwidth=0.8, relheight=1)
self.CoffeeCategory = Frame(OrderFrame, background="#E7E0D6")
self.CoffeeCategory.place(relx=0, rely=0.27, relwidth=0.95, relheight=1)
self.CoffeeCategoryLabel = Label(self.CoffeeCategory, text="Coffee Menu", bg="#E7E0D6", fg="#27150C", font=("century gothic bold", 20))
self.CoffeeCategoryLabel.place(relx=0.03, rely=0.02)

AddCoffeeButtonImage = Image.open('images/cateoryaddplus.png').resize((30, 30))
AddCoffeeButtonImage = ImageTk.PhotoImage(AddCoffeeButtonImage)
AddCoffeeButtonImage_label = Label(self.CoffeeCategory, image=AddCoffeeButtonImage, background='#DDD2C3')
AddCoffeeButtonImage_label.image = AddCoffeeButtonImage
self.AddCoffeeButton = Button(self.CoffeeCategory, text="Add New Dish to \nCoffee", background="#DDD2C3", cursor="hand2", relief="solid", activebackground="#EDD6B3", bd=1, image=AddCoffeeButtonImage, compound="top", font=("century gothic bold", 12), pady=20)
self.AddCoffeeButton.place(relx=0.03, rely=0.08, relwidth=0.21, relheight=0.24)
# Parent Frame
self.CoffeeCategory = tk.Frame(root, background="#DDD2C3")
self.CoffeeCategory.pack(fill="both", expand=True)

# Number of frames to place in a row
max_columns = 3

# Add Product Frames Dynamically
product_data = [
    ("Coffee", 'images/coffee.png'),
    ("Tea", 'images/tea.png'),
    ("Latte", 'images/latte.png'),
    ("Cappuccino", 'images/cappuccino.png'),
    ("Mocha", 'images/mocha.png')
]

for idx, (name, image_path) in enumerate(product_data):
    row = idx // max_columns  # Determine the row
    col = idx % max_columns   # Determine the column
    
    # Calculate relative x and y positions
    relx = col * 0.33  # 33% for each column (3 columns per row)
    rely = 0.1 + (row * 0.3)  # Stagger y position for each row

    # Product Frame
    ProductCard = tk.Frame(self.CoffeeCategory, background="#DDD2C3")
    ProductCard.place(relx=relx, rely=rely, relwidth=0.28, relheight=0.2)

    # Product Image
    ProductCardImage = Image.open(image_path).resize((75, 75))
    ProductCardImage = ImageTk.PhotoImage(ProductCardImage)
    ProductCardImage_label = tk.Label(ProductCard, image=ProductCardImage, background='#DDD2C3')
    ProductCardImage_label.image = ProductCardImage
    ProductCardImage_label.place(relx=0.3, rely=0.1, width=75, height=75)

    # Product Category Label
    ProductCategoryLabel = tk.Label(ProductCard, text=name, bg="#DDD2C3", fg="#27150C", font=("century gothic", 8))
    ProductCategoryLabel.place(relx=0, rely=0.56, relwidth=0.32, relheight=0.09)

    # Product Name Label
    ProductNameLabel = tk.Label(ProductCard, text=f"Hello {name}!", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 13), anchor="w")
    ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)

    # Add to Cart Button
    ProductAddToCartButton = tk.Button(ProductCard, text="Add to Cart", font=("century gothic bold", 11), width=27, height=1, background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
    ProductAddToCartButton.place(relx=0.05, rely=0.78, relwidth=0.9, relheight=0.17)

root.mainloop()
