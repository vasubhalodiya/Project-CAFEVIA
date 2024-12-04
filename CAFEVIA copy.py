from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from tkinter import filedialog
import MySQLdb

primary_color = "#27150C"
secondary_color = "#E7E0D6"
sidecart_color = "#DDD2C3"
active_color = "#EDD6B3"
price_color = "#B26431"
# ============= Blue theme color ============
# primary_color = "#221D20"
# secondary_color = "#F3F3F3"
# sidecart_color = "#E0E3EB"
# active_color = active_color #not define
# price_color = price_color #not define
# card_color = "#E4E4E7" #or #E0E3EB
# cardimg_color = "#D7DAE2" #or #F3F3F3


# def loading_screen():
#     window = Tk()
#     width = 370
#     height = 230
#     x = (window.winfo_screenwidth()//2)-(width//2)
#     y = (window.winfo_screenheight()//2)-(height//2)
#     window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#     window.overrideredirect(True)
#     window.configure(bg=secondary_color)

#     # text = "CAFEVIA"
#     # spaced_text = " ".join(text)

#     loading_text = Label(window, text="CAFEVIA", font=("century gothic bold", 30), bg=secondary_color, fg=primary_color)
#     loading_text.place(relx=0.5, rely=0.5, anchor=CENTER)
    
#     def redirectToHome():
#         window.destroy()
#         AdminDashboard()

#     window.after(3000, redirectToHome)
#     window.mainloop()

# loading_screen()

class Login():
    def __init__(self,loginwindow):
        self.loginwindow = loginwindow
        self.loginwindow.title("LOGIN - CAFEVIA")
        width = 1000
        height = 600
        x = (loginwindow.winfo_screenwidth()//2)-(width//2)
        y = (loginwindow.winfo_screenheight()//2)-(height//2)
        self.loginwindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.loginwindow.state('normal')
        self.loginwindow.resizable(False, False)
        self.loginwindow.config(background=secondary_color)

        loginimage = Image.open('images/login_img.jpg')
        loginimage = ImageTk.PhotoImage(loginimage)
        loginimage_label = Label(self.loginwindow, image=loginimage,  background=secondary_color)
        loginimage_label.image = loginimage
        loginimage_label.place(relx=0, rely=0, relwidth=0.57, relheight=1)

        #Use Verification
        name_var = StringVar()
        passw_var = StringVar()

        loginform = Frame(loginwindow, background=secondary_color)
        loginform.place(relx=0.37, rely=0, relwidth=0.63, relheight=1)

        loginwindow.overrideredirect(True)
        def close_button():
            loginwindow.destroy() 
        closebutton = Button(loginform, text="x", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=close_button)
        closebutton.place(relx=0.94, rely=0.014, width=30, height=30)
        
        # login logo
        loginlogo = Label(loginform, text="CAFEVIA", bg=secondary_color, fg=primary_color, font=("century gothic bold", 30), bd=0)
        loginlogo.place(relx=0.35, rely=0.07)
        loginslogan = Label(loginform, text="Wake up, sip, and conquer your day with our brew.", bg=secondary_color, fg=primary_color, font=("century gothic", 10))
        loginslogan.place(relx=0.23, rely=0.15)

        loginUserlabel = Label(loginform, text="Username", bg=secondary_color, fg=primary_color, font=("century gothic bold", 16))
        loginUserlabel.place(relx=0.2, rely=0.3)
        txtProductName = Entry(loginform, textvariable="name_var", font=("century gothic", 13), relief='ridge', bd=2)
        txtProductName.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.065)

        loginPasswordlabel = Label(loginform, text="Password", bg=secondary_color, fg=primary_color, font=("century gothic bold", 16))
        loginPasswordlabel.place(relx=0.2, rely=0.46)
        loginPasswordentry = Entry(loginform, textvariable="passw_var", font=("century gothic", 13), relief='ridge', bd=2, show='*')
        loginPasswordentry.place(relx=0.2, rely=0.51, relwidth=0.6, relheight=0.065)

        login = Button(loginform, text="Login", font=("century gothic bold", 15), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", bd=2, command=submit)
        login.place(relx=0.2, rely=0.68, relwidth=0.6, relheight=0.065)
        loginNote = Label(loginform, text="Must do check USERNAME & PASSWORD is correct", bg=secondary_color, fg=primary_color, font=("century gothic", 8))
        loginNote.place(relx=0.2, rely=0.755, relwidth=0.6, relheight=0.015)

        def Submit(name, passv):
            mylabel = Label(loginform, text = name + passv).pack()

def submit():
    loginwindow.destroy()
    win()


class AdminDashboard():
    def __init__(self,window):
        self.window = window
        self.window.title("CAFEVIA")
        # self.window.geometry("1500x750")
        self.window.state('zoomed')
        self.window.resizable(False, False)
        self.window.config(background=secondary_color)

        # sidebar
        self.sidebar = Frame(self.window, bg=primary_color)
        self.sidebar.place(relx=0, rely=0, relwidth=0.18, relheight=1) 

        # logoimage = Image.open('images/logo.png').resize((60, 60))
        # logoimage = ImageTk.PhotoImage(logoimage)
        # logoimage_label = Label(self.sidebar, image=logoimage, background=primary_color)
        # logoimage_label.image = logoimage
        # logoimage_label.place(relx=0, rely=0.09, width=75, height=75)
        text = "CAFEVIA"
        spaced_text = " ".join(text)

        loading_text = Label(self.sidebar, text=spaced_text, font=("century gothic bold", 27), bg=primary_color, fg=secondary_color)
        loading_text.place(relx=0.1, rely=0.07)

        # Dashboard Button

        DashboardButton = Button(self.sidebar, text="Dashboard", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(DashboardMenu))
        DashboardButton.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.05)

        MenuButton = Button(self.sidebar, text="Menu", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(MenuMenu))
        MenuButton.place(relx=0.1, rely=0.28, relwidth=0.8, relheight=0.05)

        BillingButton = Button(self.sidebar, text="Billing", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(BillingMenu))
        BillingButton.place(relx=0.1, rely=0.36, relwidth=0.8, relheight=0.05)

        OrderButton = Button(self.sidebar, text="Orders", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(OrderMenu))
        OrderButton.place(relx=0.1, rely=0.44, relwidth=0.8, relheight=0.05)

        TableBookButton = Button(self.sidebar, text="Table Book", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(TableBookMenu))
        TableBookButton.place(relx=0.1, rely=0.52, relwidth=0.8, relheight=0.05)

        SalesButton = Button(self.sidebar, text="Sales", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(SalesMenu))
        SalesButton.place(relx=0.1, rely=0.60, relwidth=0.8, relheight=0.05)

        LogoutButton = Button(self.sidebar, text="Logout", font=("century gothic bold", 11), width=27, height=1, background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=lambda:MenuSystem(LogoutMenu))
        LogoutButton.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.05)

        # Functionality for menu system
        main_frame = Frame(window, background=secondary_color)
        main_frame.place(relx=0.18, rely=0, relwidth=0.82, relheight=1)

        HomeImage = Image.open('images/homeimg.jpg')
        HomeImage = ImageTk.PhotoImage(HomeImage)
        HomeImage_label = Label(main_frame, image=HomeImage, background=sidecart_color)
        HomeImage_label.image = HomeImage
        HomeImage_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.HomeLabel = Label(main_frame, text="Welcome to CAFEVIA", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 25))
        self.HomeLabel.place(relx=0.35, rely=0.18)

# ===========================================================================================

        def MenuSystem(page):
            for frame in main_frame.winfo_children():
                frame.destroy()
            page()

        def DashboardMenu():
            DashboardFrame = Frame(main_frame, background='red')
            DashboardFrame.place(relx=0, rely=0, relwidth=1, relheight=1)





        # ==========================================

        def MenuMenu():
            MenuFrame = Frame(main_frame, background=secondary_color)
            MenuFrame.place(relx=0, rely=0, relwidth=0.8, relheight=1)

        # ================== Menu Cart Product Start=====================
            MenuCartFrame = Frame(main_frame, background=sidecart_color)
            MenuCartFrame.place(relx=0.76, rely=0, relwidth=0.24, relheight=1)
            
            MenuCartItem = Label(MenuCartFrame, text="Cart", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 20))
            MenuCartItem.place(relx=0.03, rely=0.01)

            MenuCartOrderNo = Label(MenuCartFrame, text="Order #3243", bg=sidecart_color, fg=primary_color, font=("century gothic", 10))
            MenuCartOrderNo.place(relx=0.7, rely=0.02)

            MenuCartDineInBtn = Button(MenuCartFrame, text="Dine In", font=("century gothic bold", 11), background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            MenuCartDineInBtn.place(relx=0.05, rely=0.07, relwidth=0.25, relheight=0.04)

            MenuCartTakeAwayBtn = Button(MenuCartFrame, text="Take away", font=("century gothic bold", 11), background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            MenuCartTakeAwayBtn.place(relx=0.35, rely=0.07, relwidth=0.35, relheight=0.04)

            MenuCartProductCardParent = Frame(MenuCartFrame, background=sidecart_color)
            MenuCartProductCardParent.place(relx=0.05, rely=0.16, relwidth=0.91, relheight=0.11)

            MenuCartProductImage = Image.open('images/coffee.png').resize((60, 60))
            MenuCartProductImage = ImageTk.PhotoImage(MenuCartProductImage)
            MenuCartProductImage_label = Label(MenuCartProductCardParent, image=MenuCartProductImage, background=sidecart_color)
            MenuCartProductImage_label.image = MenuCartProductImage
            MenuCartProductImage_label.place(relx=0, rely=0.09, width=75, height=75)

            MenuCartProductName = Label(MenuCartProductCardParent, text="Hello World Coffee", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13))
            MenuCartProductName.place(relx=0.3, rely=0.1)

            MenuCartOrderPrice = Label(MenuCartProductCardParent, text="₹ 100", bg=price_color, fg=secondary_color, font=("century gothic bold", 13))
            MenuCartOrderPrice.place(relx=0.32, rely=0.5, relwidth=0.21, relheight=0.24)

            MenuCartMinusBtn = Button(MenuCartProductCardParent, text="-", font=("century gothic bold", 15), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            MenuCartMinusBtn.place(relx=0.6, rely=0.5, width=25, height=25)
            # *************
            MenuCartItemNo = Label(MenuCartProductCardParent, text="3", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 15))
            MenuCartItemNo.place(relx=0.7, rely=0.5, width=22, height=22)
            # *************
            MenuCartPlusBtn = Button(MenuCartProductCardParent, text="+", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            MenuCartPlusBtn.place(relx=0.8, rely=0.5, width=25, height=25)
        # ===================================================
            MenuCartProductCardParent = Frame(MenuCartFrame, background=sidecart_color)
            MenuCartProductCardParent.place(relx=0.05, rely=0.3, relwidth=0.91, relheight=0.11)

            MenuCartProductImage = Image.open('images/coffee.png').resize((60, 60))
            MenuCartProductImage = ImageTk.PhotoImage(MenuCartProductImage)
            MenuCartProductImage_label = Label(MenuCartProductCardParent, image=MenuCartProductImage, background=sidecart_color)
            MenuCartProductImage_label.image = MenuCartProductImage
            MenuCartProductImage_label.place(relx=0, rely=0.09, width=75, height=75)

            MenuCartProductName = Label(MenuCartProductCardParent, text="Hello World Coffee", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13))
            MenuCartProductName.place(relx=0.3, rely=0.1)

            MenuCartOrderPrice = Label(MenuCartProductCardParent, text="₹ 100", bg=price_color, fg=secondary_color, font=("century gothic bold", 13))
            MenuCartOrderPrice.place(relx=0.32, rely=0.5, relwidth=0.21, relheight=0.24)

            MenuCartMinusBtn = Button(MenuCartProductCardParent, text="-", font=("century gothic bold", 15), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            MenuCartMinusBtn.place(relx=0.6, rely=0.5, width=25, height=25)
            # *************
            MenuCartItemNo = Label(MenuCartProductCardParent, text="3", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 15))
            MenuCartItemNo.place(relx=0.7, rely=0.5, width=22, height=22)
            # *************
            MenuCartPlusBtn = Button(MenuCartProductCardParent, text="+", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            MenuCartPlusBtn.place(relx=0.8, rely=0.5, width=25, height=25)
        # ===================================================

            MenuCartItemTotal = Label(MenuCartFrame, text="Items", bg=sidecart_color, fg=primary_color, font=("century gothic", 11), anchor="w")
            MenuCartItemTotal.place(relx=0.05, rely=0.77, relwidth=0.2, relheight=0.03)
            MenuCartItemTotalAns = Label(MenuCartFrame, text="₹ 1000", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 12), anchor="e")
            MenuCartItemTotalAns.place(relx=0.7, rely=0.77, relwidth=0.25, relheight=0.03)
            # *************
            MenuCartDiscountTotal = Label(MenuCartFrame, text="Discount", bg=sidecart_color, fg=primary_color, font=("century gothic", 11), anchor="w")
            MenuCartDiscountTotal.place(relx=0.05, rely=0.81, relwidth=0.25, relheight=0.03)
            MenuCartDiscountTotalAns = Label(MenuCartFrame, text="- ₹100", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 12), anchor="e")
            MenuCartDiscountTotalAns.place(relx=0.75, rely=0.81, relwidth=0.2, relheight=0.03)

            # *************
            MenuCartTotalFrame = Frame(MenuCartFrame, background=sidecart_color)
            MenuCartTotalFrame.place(relx=0.05, rely=0.86, relwidth=0.9, relheight=0.14)
            top_border = Frame(MenuCartTotalFrame, bg="#CBA084", height=1)
            top_border.pack(side="top", fill="x")
            # *************
            MenuCartAllTotal = Label(MenuCartTotalFrame, text="Total", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 12), anchor="w")
            MenuCartAllTotal.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.2)
            MenuCartAllTotalAns = Label(MenuCartTotalFrame, text="₹ 1000", bg=price_color, fg=secondary_color, font=("century gothic bold", 12))
            MenuCartAllTotalAns.place(relx=0.73, rely=0.2, relwidth=0.28, relheight=0.2)
            # *************
            MenuCartPlaceOrderBtn = Button(MenuCartTotalFrame, text="Place an order", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            MenuCartPlaceOrderBtn.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)



        # ================== Menu Cart Product End=====================

            ChooseCategory = Label(MenuFrame, text="Choose Category", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            ChooseCategory.place(relx=0.03, rely=0.02)

            # ============================
            # categoryimage = Image.open('images/all.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # CategoryChildCard = Button(MenuFrame, text="All", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # CategoryChildCard.place(relx=0.03, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/coffee.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # CategoryChildCard = Button(MenuFrame, text="Coffee", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # CategoryChildCard.place(relx=0.16, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/softdrink.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # CategoryChildCard = Button(MenuFrame, text="Softdrink", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # CategoryChildCard.place(relx=0.29, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/pizza.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # CategoryChildCard = Button(MenuFrame, text="Pizza", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # CategoryChildCard.place(relx=0.42, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/burger.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # CategoryChildCard = Button(MenuFrame, text="Burger", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # CategoryChildCard.place(relx=0.55, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/dessert.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # CategoryChildCard = Button(MenuFrame, text="Dessert", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # CategoryChildCard.place(relx=0.68, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/meal.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # CategoryChildCard = Button(MenuFrame, text="Food Meal", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # CategoryChildCard.place(relx=0.81, rely=0.08, width=110, height=110)
            # # ============================

            categories = [
                {"name": "All", "image": "images/all.png"},
                {"name": "Coffee", "image": "images/coffee.png"},
                {"name": "Softdrink", "image": "images/softdrink.png"},
                {"name": "Pizza", "image": "images/pizza.png"},
                {"name": "Burger", "image": "images/burger.png"},
                {"name": "Dessert", "image": "images/dessert.png"},
                {"name": "Food Meal", "image": "images/meal.png"},
            ]

            for i, category in enumerate(categories):
                category_image = Image.open(category["image"]).resize((45, 45))
                category_image = ImageTk.PhotoImage(category_image)
                
                relx = 0.03 + i * 0.13
                
                CategoryChildCard = Button(MenuFrame, text=category["name"], image=category_image, background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, compound="top", font=("century gothic bold", 12), pady=13)
                CategoryChildCard.image = category_image
                CategoryChildCard.place(relx=relx, rely=0.08, width=110, height=110)
           
# =============================================================================================

            CoffeeCategory = Frame(MenuFrame, background=secondary_color)
            CoffeeCategory.place(relx=0, rely=0.27, relwidth=0.95, relheight=1)
            CoffeeCategoryLabel = Label(CoffeeCategory, text="Coffee Menu", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            CoffeeCategoryLabel.place(relx=0.03, rely=0.02)

    # ================= add coffee button =======================
            AddCoffeeButtonImage = Image.open('images/cateoryaddplus.png').resize((30, 30))
            AddCoffeeButtonImage = ImageTk.PhotoImage(AddCoffeeButtonImage)
            AddCoffeeButtonImage_label = Label(CoffeeCategory, image=AddCoffeeButtonImage, background=sidecart_color)
            AddCoffeeButtonImage_label.image = AddCoffeeButtonImage

            AddCoffeeButton = Button(CoffeeCategory, text="Add New Dish to \nCoffee", background=sidecart_color, cursor="hand2", relief="solid", activebackground=active_color, bd=1, image=AddCoffeeButtonImage, compound="top", font=("century gothic bold", 12), pady=20, command=fetch_products)
            AddCoffeeButton.place(relx=0.03, rely=0.08, relwidth=0.21, relheight=0.25)

    # ===================================================================================================
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

    # ===================================================================================================
            ProductCard = Frame(CoffeeCategory, background=sidecart_color)
            ProductCard.place(relx=0.515, rely=0.08, relwidth=0.21, relheight=0.25)
            # *********************
            ProductCardImage = Image.open('images/coffee.png').resize((75, 75))
            ProductCardImage = ImageTk.PhotoImage(ProductCardImage)
            ProductCardImage_label = Label(ProductCard, image=ProductCardImage, background=sidecart_color)
            ProductCardImage_label.image = ProductCardImage
            ProductCardImage_label.place(relx=0.3, rely=0.1, width=75, height=75)
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

    # ===================================================================================================
            ProductCard = Frame(CoffeeCategory, background=sidecart_color)
            ProductCard.place(relx=0.76, rely=0.08, relwidth=0.21, relheight=0.25)
            # *********************
            ProductCardImage = Image.open('images/coffee.png').resize((75, 75))
            ProductCardImage = ImageTk.PhotoImage(ProductCardImage)
            ProductCardImage_label = Label(ProductCard, image=ProductCardImage, background=sidecart_color)
            ProductCardImage_label.image = ProductCardImage
            ProductCardImage_label.place(relx=0.3, rely=0.1, width=75, height=75)
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

# =========================================================================================================

        def ProductMenu():
            AddCoffeeWindow = Tk()
            AddCoffeeWindow.title("Add Coffee - CAFEVIA")
            width = 1200
            height = 750
            x = (AddCoffeeWindow.winfo_screenwidth() // 2) - (width // 2)
            y = (AddCoffeeWindow.winfo_screenheight() // 2) - (height // 2)
            AddCoffeeWindow.geometry(f'{width}x{height}+{x}+{y}')
            AddCoffeeWindow.resizable(False, False)
            AddCoffeeWindow.config(background=secondary_color)

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
                    cursor.execute("INSERT INTO product (proname, procategory, proavailable, proprice, proimage) VALUES (%s, %s, %s, %s, %s)", (ProductName, ProductCategory, ProductAvaliable, ProductPrice, ProductImage))
                    con.commit()

                    txtProductName.delete(0,'end')
                    txtProductCategory.delete(0,'end')
                    txtProductAvaliable.delete(0,'end')
                    txtProductPrice.delete(0,'end')
                    txtProductImage.delete(0,'end')
                    messagebox.showinfo("INSERT Status","INSERTED SUCCESSFULLY")
                    con.close()

        def fetch_products():
            con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM product")
            products = cursor.fetchall()
            con.close()

            # Clear the existing cards (if any)
            for widget in canvas_frame.winfo_children():
                widget.destroy()

            # Display each product in a new card
            row_frame = None
            card_count = 0
            for product in products:
                if card_count % 3 == 0:  # Create a new row for every 3 cards
                    row_frame = Frame(canvas_frame)
                    row_frame.pack(pady=10)

                ProductCard = Frame(row_frame, background=sidecart_color, bd=1, relief="solid", width=300, height=200)
                ProductCard.grid(row=0, column=card_count % 3, padx=10)

                # Image
                

                # Category
                ProductCategoryLabel = Label(ProductCard, text=product[2], bg=sidecart_color, fg=primary_color, font=("century gothic", 8))
                ProductCategoryLabel.place(relx=0, rely=0.56, relwidth=0.32, relheight=0.09)

                # Product Name
                ProductNameLabel = Label(ProductCard, text=product[1], bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13), anchor="w")
                ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)

                # Price
                ProductPriceLabel = Label(ProductCard, text=f"₹ {product[3]}", bg=price_color, fg=sidecart_color, font=("century gothic bold", 15))
                ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)

                # Add to Cart Button
                ProductAddToCardButton = Button(ProductCard, text="Add", font=("century gothic bold", 11), width=27, height=1, background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
                ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)

                card_count += 1

            # After adding cards, update the scrollregion to fit all the cards
            canvas.config(scrollregion=canvas.bbox("all"))

        root = Tk()
        root.title("Product Management - CAFEVIA")
        width = 1200
        height = 750
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')
        root.resizable(False, False)
        root.config(background=secondary_color)


        AddNavbar = Frame(root, background=primary_color)
        AddNavbar.place(relx=0, rely=0, relwidth=1, relheight=0.5)

        # Title Label
        AddHeadLabel = Label(root, text="Add Product", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
        AddHeadLabel.place(relx=0, rely=0.02, relwidth=1, relheight=0.05)

        # Form fields (Product ID, Category, etc.)
        txtProductId = Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
        txtProductId.place(relx=0.07, rely=0.15, relwidth=0.25, relheight=0.05)

        txtProductCategory = Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
        txtProductCategory.place(relx=0.07, rely=0.28, relwidth=0.25, relheight=0.05)

        txtProductAvaliable = Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
        txtProductAvaliable.place(relx=0.07, rely=0.41, relwidth=0.25, relheight=0.05)

        txtProductName = Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
        txtProductName.place(relx=0.4, rely=0.15, relwidth=0.25, relheight=0.05)

        txtProductPrice = Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
        txtProductPrice.place(relx=0.4, rely=0.28, relwidth=0.25, relheight=0.05)

        txtProductImage = Entry(root, font=("century gothic", 13), relief='ridge', bd=2)
        txtProductImage.place(relx=0.4, rely=0.41, relwidth=0.25, relheight=0.05)

        # Add Product Button
        AddProductButton = Button(root, text="Add Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12))
        AddProductButton.place(relx=0.73, rely=0.12, relwidth=0.2, relheight=0.08)

        # Create a canvas for scrolling
        canvas = Canvas(root)
        canvas.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

        # Create a vertical scrollbar linked to the canvas
        scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollbar.place(relx=0.97, rely=0.5, relwidth=0.03, relheight=0.5)

        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the product cards
        canvas_frame = Frame(canvas)
        canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

        # Fetch and display products on startup
        fetch_products()


        # ==========================================

        def BillingMenu():
            BillingFrame = Frame(main_frame, background='green')
            BillingFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ==========================================

        def OrderMenu():
            OrderFrame = Frame(main_frame, background='green')
            OrderFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ==========================================

        def TableBookMenu():
            TableBookFrame = Frame(main_frame, background='yellow')
            TableBookFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ==========================================

        def SalesMenu():
            SalesFrame = Frame(main_frame, background='darkred')
            SalesFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ==========================================

        def LogoutMenu():
            self.window.destroy()

        # ==========================================











































def win():
    window = Tk()
    AdminDashboard(window)
    window.mainloop()

if __name__ == '__main__':

    # loginwindow = Tk()
    # Login(loginwindow)
    # loginwindow.mainloop()
    win()






































