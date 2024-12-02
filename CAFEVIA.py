from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

# def loading_screen():
#     window = Tk()
#     width = 370
#     height = 230
#     x = (window.winfo_screenwidth()//2)-(width//2)
#     y = (window.winfo_screenheight()//2)-(height//2)
#     window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#     window.overrideredirect(True)
#     window.configure(bg="#E7E0D6")

#     # text = "CAFEVIA"
#     # spaced_text = " ".join(text)

#     loading_text = Label(window, text="CAFEVIA", font=("century gothic bold", 30), bg="#E7E0D6", fg="#27150C")
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
        self.loginwindow.config(background='#E7E0D6')

        self.loginback = Frame(loginwindow, background="#E7E0D6")
        self.loginback.place(relx=0, rely=0, relwidth=1, relheight=1)

        loginimage = Image.open('images/login_img.jpg')
        loginimage = ImageTk.PhotoImage(loginimage)
        loginimage_label = Label(self.loginback, image=loginimage,  background="#E7E0D6")
        loginimage_label.image = loginimage
        loginimage_label.place(relx=0, rely=0, relwidth=0.57, relheight=1)

        #Use Verification
        name_var = StringVar()
        passw_var = StringVar()

        self.loginform = Frame(loginwindow, background="#E7E0D6")
        self.loginform.place(relx=0.37, rely=0, relwidth=0.63, relheight=1)

        loginwindow.overrideredirect(True)
        def close_button():
            loginwindow.destroy() 
        self.closebutton = Button(self.loginform, text="x", font=("century gothic bold", 13), background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=close_button)
        self.closebutton.place(relx=0.94, rely=0.014, width=30, height=30)
        
        # login logo
        self.loginlogo = Label(self.loginform, text="CAFEVIA", bg="#E7E0D6", fg="#27150C", font=("century gothic bold", 30), bd=0)
        self.loginlogo.place(relx=0.35, rely=0.07)
        self.loginslogan = Label(self.loginform, text="Wake up, sip, and conquer your day with our brew.", bg="#E7E0D6", fg="#27150C", font=("century gothic", 10))
        self.loginslogan.place(relx=0.23, rely=0.15)

        self.loginUserlabel = Label(self.loginform, text="Username", bg="#E7E0D6", fg="#27150C", font=("century gothic bold", 16))
        self.loginUserlabel.place(relx=0.2, rely=0.3)
        self.loginUserentry = Entry(self.loginform, textvariable="name_var", font=("century gothic", 13), relief='ridge', bd=2)
        self.loginUserentry.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.065)

        self.loginPasswordlabel = Label(self.loginform, text="Password", bg="#E7E0D6", fg="#27150C", font=("century gothic bold", 16))
        self.loginPasswordlabel.place(relx=0.2, rely=0.46)
        self.loginPasswordentry = Entry(self.loginform, textvariable="passw_var", font=("century gothic", 13), relief='ridge', bd=2, show='*')
        self.loginPasswordentry.place(relx=0.2, rely=0.51, relwidth=0.6, relheight=0.065)

        self.login = Button(self.loginform, text="Login", font=("century gothic bold", 15), background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", bd=2, command=submit)
        self.login.place(relx=0.2, rely=0.68, relwidth=0.6, relheight=0.065)
        self.loginNote = Label(self.loginform, text="Must do check USERNAME & PASSWORD is correct", bg="#E7E0D6", fg="#27150C", font=("century gothic", 8))
        self.loginNote.place(relx=0.2, rely=0.755, relwidth=0.6, relheight=0.015)

        def Submit(name, passv):
            mylabel = Label(self.loginform, text = name + passv).pack()

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
        self.window.config(background='#E7E0D6')

        # sidebar
        self.sidebar = Frame(self.window, bg='#27150C')
        self.sidebar.place(relx=0, rely=0, relwidth=0.18, relheight=1) 

        # logoimage = Image.open('images/logo.png').resize((60, 60))
        # logoimage = ImageTk.PhotoImage(logoimage)
        # logoimage_label = Label(self.sidebar, image=logoimage, background='#27150C')
        # logoimage_label.image = logoimage
        # logoimage_label.place(relx=0, rely=0.09, width=75, height=75)
        text = "CAFEVIA"
        spaced_text = " ".join(text)

        loading_text = Label(self.sidebar, text=spaced_text, font=("century gothic bold", 27), bg="#27150C", fg="#E7E0D6")
        loading_text.place(relx=0.1, rely=0.07)

        DashboardButton = Button(self.sidebar, text="Dashboard", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(DashboardMenu))
        DashboardButton.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.05)

        MenuButton = Button(self.sidebar, text="Menu", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(MenuMenu))
        MenuButton.place(relx=0.1, rely=0.28, relwidth=0.8, relheight=0.05)

        BillingButton = Button(self.sidebar, text="Billing", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(BillingMenu))
        BillingButton.place(relx=0.1, rely=0.36, relwidth=0.8, relheight=0.05)

        OrderButton = Button(self.sidebar, text="Orders", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(OrderMenu))
        OrderButton.place(relx=0.1, rely=0.44, relwidth=0.8, relheight=0.05)

        TableBookButton = Button(self.sidebar, text="Table Book", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(TableBookMenu))
        TableBookButton.place(relx=0.1, rely=0.52, relwidth=0.8, relheight=0.05)

        SalesButton = Button(self.sidebar, text="Sales", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(SalesMenu))
        SalesButton.place(relx=0.1, rely=0.60, relwidth=0.8, relheight=0.05)

        LogoutButton = Button(self.sidebar, text="Logout", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(LogoutMenu))
        LogoutButton.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.05)

        # Functionality for menu system
        main_frame = Frame(window, background='#E7E0D6')
        main_frame.place(relx=0.18, rely=0, relwidth=0.82, relheight=1)

        HomeImage = Image.open('images/homeimg.jpg')
        HomeImage = ImageTk.PhotoImage(HomeImage)
        HomeImage_label = Label(main_frame, image=HomeImage, background='#DDD2C3')
        HomeImage_label.image = HomeImage
        HomeImage_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.HomeLabel = Label(main_frame, text="Welcome to CAFEVIA", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 25))
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
            MenuFrame = Frame(main_frame, background='#E7E0D6')
            MenuFrame.place(relx=0, rely=0, relwidth=0.8, relheight=1)

        # ================== Menu Cart Product Start=====================
            MenuCartFrame = Frame(main_frame, background='#DDD2C3')
            MenuCartFrame.place(relx=0.76, rely=0, relwidth=0.24, relheight=1)
            
            self.MenuCartItem = Label(MenuCartFrame, text="Cart", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 20))
            self.MenuCartItem.place(relx=0.03, rely=0.01)

            self.MenuCartOrderNo = Label(MenuCartFrame, text="Order #3243", bg="#DDD2C3", fg="#27150C", font=("century gothic", 10))
            self.MenuCartOrderNo.place(relx=0.7, rely=0.02)

            self.MenuCartDineInBtn = Button(MenuCartFrame, text="Dine In", font=("century gothic bold", 11), background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.MenuCartDineInBtn.place(relx=0.05, rely=0.07, relwidth=0.25, relheight=0.04)

            self.MenuCartTakeAwayBtn = Button(MenuCartFrame, text="Take away", font=("century gothic bold", 11), background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.MenuCartTakeAwayBtn.place(relx=0.35, rely=0.07, relwidth=0.35, relheight=0.04)

            self.MenuCartProductCardParent = Frame(MenuCartFrame, background='#DDD2C3')
            self.MenuCartProductCardParent.place(relx=0.05, rely=0.16, relwidth=0.91, relheight=0.11)

            MenuCartProductImage = Image.open('images/coffee.png').resize((60, 60))
            MenuCartProductImage = ImageTk.PhotoImage(MenuCartProductImage)
            MenuCartProductImage_label = Label(self.MenuCartProductCardParent, image=MenuCartProductImage, background='#DDD2C3')
            MenuCartProductImage_label.image = MenuCartProductImage
            MenuCartProductImage_label.place(relx=0, rely=0.09, width=75, height=75)

            self.MenuCartProductName = Label(self.MenuCartProductCardParent, text="Hello World Coffee", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 13))
            self.MenuCartProductName.place(relx=0.3, rely=0.1)

            self.MenuCartOrderPrice = Label(self.MenuCartProductCardParent, text="₹ 100", bg="#B26431", fg="#E7E0D6", font=("century gothic bold", 13))
            self.MenuCartOrderPrice.place(relx=0.32, rely=0.5, relwidth=0.21, relheight=0.24)

            self.MenuCartMinusBtn = Button(self.MenuCartProductCardParent, text="-", font=("century gothic bold", 15), background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.MenuCartMinusBtn.place(relx=0.6, rely=0.5, width=25, height=25)
            # *************
            self.MenuCartItemNo = Label(self.MenuCartProductCardParent, text="3", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 15))
            self.MenuCartItemNo.place(relx=0.7, rely=0.5, width=22, height=22)
            # *************
            self.MenuCartPlusBtn = Button(self.MenuCartProductCardParent, text="+", font=("century gothic bold", 13), background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.MenuCartPlusBtn.place(relx=0.8, rely=0.5, width=25, height=25)
        # ===================================================
            self.MenuCartProductCardParent = Frame(MenuCartFrame, background='#DDD2C3')
            self.MenuCartProductCardParent.place(relx=0.05, rely=0.3, relwidth=0.91, relheight=0.11)

            MenuCartProductImage = Image.open('images/coffee.png').resize((60, 60))
            MenuCartProductImage = ImageTk.PhotoImage(MenuCartProductImage)
            MenuCartProductImage_label = Label(self.MenuCartProductCardParent, image=MenuCartProductImage, background='#DDD2C3')
            MenuCartProductImage_label.image = MenuCartProductImage
            MenuCartProductImage_label.place(relx=0, rely=0.09, width=75, height=75)

            self.MenuCartProductName = Label(self.MenuCartProductCardParent, text="Hello World Coffee", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 13))
            self.MenuCartProductName.place(relx=0.3, rely=0.1)

            self.MenuCartOrderPrice = Label(self.MenuCartProductCardParent, text="₹ 100", bg="#B26431", fg="#E7E0D6", font=("century gothic bold", 13))
            self.MenuCartOrderPrice.place(relx=0.32, rely=0.5, relwidth=0.21, relheight=0.24)

            self.MenuCartMinusBtn = Button(self.MenuCartProductCardParent, text="-", font=("century gothic bold", 15), background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.MenuCartMinusBtn.place(relx=0.6, rely=0.5, width=25, height=25)
            # *************
            self.MenuCartItemNo = Label(self.MenuCartProductCardParent, text="3", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 15))
            self.MenuCartItemNo.place(relx=0.7, rely=0.5, width=22, height=22)
            # *************
            self.MenuCartPlusBtn = Button(self.MenuCartProductCardParent, text="+", font=("century gothic bold", 13), background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.MenuCartPlusBtn.place(relx=0.8, rely=0.5, width=25, height=25)
        # ===================================================

            self.MenuCartItemTotal = Label(MenuCartFrame, text="Items", bg="#DDD2C3", fg="#27150C", font=("century gothic", 11), anchor="w")
            self.MenuCartItemTotal.place(relx=0.05, rely=0.77, relwidth=0.2, relheight=0.03)
            self.MenuCartItemTotalAns = Label(MenuCartFrame, text="₹ 1000", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 12), anchor="e")
            self.MenuCartItemTotalAns.place(relx=0.7, rely=0.77, relwidth=0.25, relheight=0.03)
            # *************
            self.MenuCartDiscountTotal = Label(MenuCartFrame, text="Discount", bg="#DDD2C3", fg="#27150C", font=("century gothic", 11), anchor="w")
            self.MenuCartDiscountTotal.place(relx=0.05, rely=0.81, relwidth=0.25, relheight=0.03)
            self.MenuCartDiscountTotalAns = Label(MenuCartFrame, text="- ₹100", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 12), anchor="e")
            self.MenuCartDiscountTotalAns.place(relx=0.75, rely=0.81, relwidth=0.2, relheight=0.03)

            # *************
            self.MenuCartTotalFrame = Frame(MenuCartFrame, background='#DDD2C3')
            self.MenuCartTotalFrame.place(relx=0.05, rely=0.86, relwidth=0.9, relheight=0.14)
            top_border = Frame(self.MenuCartTotalFrame, bg="#CBA084", height=1)
            top_border.pack(side="top", fill="x")
            # *************
            self.MenuCartAllTotal = Label(self.MenuCartTotalFrame, text="Total", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 12), anchor="w")
            self.MenuCartAllTotal.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.2)
            self.MenuCartAllTotalAns = Label(self.MenuCartTotalFrame, text="₹ 1000", bg="#B26431", fg="#E7E0D6", font=("century gothic bold", 12))
            self.MenuCartAllTotalAns.place(relx=0.73, rely=0.2, relwidth=0.28, relheight=0.2)
            # *************
            self.MenuCartPlaceOrderBtn = Button(self.MenuCartTotalFrame, text="Place an order", font=("century gothic bold", 13), background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.MenuCartPlaceOrderBtn.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)



        # ================== Menu Cart Product End=====================

            self.ChooseCategory = Label(MenuFrame, text="Choose Category", bg="#E7E0D6", fg="#27150C", font=("century gothic bold", 20))
            self.ChooseCategory.place(relx=0.03, rely=0.02)

            # ============================
            # categoryimage = Image.open('images/all.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background='#DDD2C3')
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="All", background="#DDD2C3", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.03, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/coffee.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background='#DDD2C3')
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Coffee", background="#DDD2C3", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.16, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/softdrink.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background='#DDD2C3')
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Softdrink", background="#DDD2C3", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.29, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/pizza.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background='#DDD2C3')
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Pizza", background="#DDD2C3", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.42, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/burger.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background='#DDD2C3')
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Burger", background="#DDD2C3", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.55, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/dessert.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background='#DDD2C3')
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Dessert", background="#DDD2C3", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.68, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/meal.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background='#DDD2C3')
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Food Meal", background="#DDD2C3", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.81, rely=0.08, width=110, height=110)
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
                
                self.CategoryChildCard = Button(MenuFrame, text=category["name"], image=category_image, background="#DDD2C3", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, compound="top", font=("century gothic bold", 12), pady=13)
                self.CategoryChildCard.image = category_image
                self.CategoryChildCard.place(relx=relx, rely=0.08, width=110, height=110)
           
# =============================================================================================

            self.CoffeeCategory = Frame(MenuFrame, background="#E7E0D6")
            self.CoffeeCategory.place(relx=0, rely=0.27, relwidth=0.95, relheight=1)
            self.CoffeeCategoryLabel = Label(self.CoffeeCategory, text="Coffee Menu", bg="#E7E0D6", fg="#27150C", font=("century gothic bold", 20))
            self.CoffeeCategoryLabel.place(relx=0.03, rely=0.02)

    # ================= add coffee button =======================
            AddCoffeeButtonImage = Image.open('images/cateoryaddplus.png').resize((30, 30))
            AddCoffeeButtonImage = ImageTk.PhotoImage(AddCoffeeButtonImage)
            AddCoffeeButtonImage_label = Label(self.CoffeeCategory, image=AddCoffeeButtonImage, background='#DDD2C3')
            AddCoffeeButtonImage_label.image = AddCoffeeButtonImage

            self.AddCoffeeButton = Button(self.CoffeeCategory, text="Add New Dish to \nCoffee", background="#DDD2C3", cursor="hand2", relief="solid", activebackground="#EDD6B3", bd=1, image=AddCoffeeButtonImage, compound="top", font=("century gothic bold", 12), pady=20, command=AddCoffeeProduct)
            self.AddCoffeeButton.place(relx=0.03, rely=0.08, relwidth=0.21, relheight=0.25)

    # ===================================================================================================
            self.ProductCard = Frame(self.CoffeeCategory, background="#DDD2C3")
            self.ProductCard.place(relx=0.27, rely=0.08, relwidth=0.21, relheight=0.25)
            # *********************
            ProductCardImage = Image.open('images/coffee.png').resize((75, 75))
            ProductCardImage = ImageTk.PhotoImage(ProductCardImage)
            ProductCardImage_label = Label(self.ProductCard, image=ProductCardImage, background='#DDD2C3')
            ProductCardImage_label.image = ProductCardImage
            ProductCardImage_label.place(relx=0.3, rely=0.08, width=75, height=75)
            # *********************
            self.ProductCategoryLabel = Label(self.ProductCard, text="Coffee", bg="#DDD2C3", fg="#27150C", font=("century gothic", 8))
            self.ProductCategoryLabel.place(relx=0, rely=0.56, relwidth=0.32, relheight=0.09)
            # *********************
            self.ProductNameLabel = Label(self.ProductCard, text="Hello World Coffee", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 13), anchor="w") # wraplength=180
            self.ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)
            # *********************
            self.ProductAddToCardButton = Button(self.ProductCard, text="Add", font=("century gothic bold", 11), width=27, height=1, background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)
            # *********************
            self.ProductPriceLabel = Label(self.ProductCard, text="₹ 100", bg="#B26431", fg="#DDD2C3", font=("century gothic bold", 15))
            self.ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)

    # ===================================================================================================
            self.ProductCard = Frame(self.CoffeeCategory, background="#DDD2C3")
            self.ProductCard.place(relx=0.515, rely=0.08, relwidth=0.21, relheight=0.25)
            # *********************
            ProductCardImage = Image.open('images/coffee.png').resize((75, 75))
            ProductCardImage = ImageTk.PhotoImage(ProductCardImage)
            ProductCardImage_label = Label(self.ProductCard, image=ProductCardImage, background='#DDD2C3')
            ProductCardImage_label.image = ProductCardImage
            ProductCardImage_label.place(relx=0.3, rely=0.1, width=75, height=75)
            # *********************
            self.ProductCategoryLabel = Label(self.ProductCard, text="Coffee", bg="#DDD2C3", fg="#27150C", font=("century gothic", 8))
            self.ProductCategoryLabel.place(relx=0, rely=0.56, relwidth=0.32, relheight=0.09)
            # *********************
            self.ProductNameLabel = Label(self.ProductCard, text="Hello World Coffee", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 13), anchor="w") # wraplength=180
            self.ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)
            # *********************
            self.ProductAddToCardButton = Button(self.ProductCard, text="Add", font=("century gothic bold", 11), width=27, height=1, background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)
            # *********************
            self.ProductPriceLabel = Label(self.ProductCard, text="₹ 100", bg="#B26431", fg="#DDD2C3", font=("century gothic bold", 15))
            self.ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)

    # ===================================================================================================
            self.ProductCard = Frame(self.CoffeeCategory, background="#DDD2C3")
            self.ProductCard.place(relx=0.76, rely=0.08, relwidth=0.21, relheight=0.25)
            # *********************
            ProductCardImage = Image.open('images/coffee.png').resize((75, 75))
            ProductCardImage = ImageTk.PhotoImage(ProductCardImage)
            ProductCardImage_label = Label(self.ProductCard, image=ProductCardImage, background='#DDD2C3')
            ProductCardImage_label.image = ProductCardImage
            ProductCardImage_label.place(relx=0.3, rely=0.1, width=75, height=75)
            # *********************
            self.ProductCategoryLabel = Label(self.ProductCard, text="Coffee", bg="#DDD2C3", fg="#27150C", font=("century gothic", 8))
            self.ProductCategoryLabel.place(relx=0, rely=0.56, relwidth=0.32, relheight=0.09)
            # *********************
            self.ProductNameLabel = Label(self.ProductCard, text="Hello World Coffee", bg="#DDD2C3", fg="#27150C", font=("century gothic bold", 13), anchor="w") # wraplength=180
            self.ProductNameLabel.place(relx=0.05, rely=0.65, relwidth=0.94, relheight=0.115)
            # *********************
            self.ProductAddToCardButton = Button(self.ProductCard, text="Add", font=("century gothic bold", 11), width=27, height=1, background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2)
            self.ProductAddToCardButton.place(relx=0.5, rely=0.78, relwidth=0.45, relheight=0.17)
            # *********************
            self.ProductPriceLabel = Label(self.ProductCard, text="₹ 100", bg="#B26431", fg="#DDD2C3", font=("century gothic bold", 15))
            self.ProductPriceLabel.place(relx=0.05, rely=0.78, relwidth=0.4, relheight=0.17)

# =========================================================================================================

        def AddCoffeeProduct():
            self.AddCoffeeWindow = Tk()
            self.AddCoffeeWindow.title("Add Coffee - CAFEVIA")
            width = 1200
            height = 750
            x = (window.winfo_screenwidth()//2)-(width//2)
            y = (window.winfo_screenheight()//2)-(height//2)
            self.AddCoffeeWindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            self.AddCoffeeWindow.state('normal')
            self.AddCoffeeWindow.resizable(False, False)
            self.AddCoffeeWindow.config(background='#E7E0D6')

            self.AddNavbar = Frame(self.AddCoffeeWindow, background='#27150C')
            self.AddNavbar.place(relx=0, rely=0, relwidth=1, relheight=0.5)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Add Coffee", bg="#E7E0D6", fg="#27150C", font=("century gothic bold", 20))
            self.AddHeadLabel.place(relx=0, rely=0.02, relwidth=1, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Name", bg="#27150C", fg="#E7E0D6", font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.07, rely=0.1)
            self.loginUserentry = Entry(self.AddCoffeeWindow, textvariable="proname_var", font=("century gothic", 13), relief='ridge', bd=2)
            self.loginUserentry.place(relx=0.07, rely=0.15, relwidth=0.25, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Category", bg="#27150C", fg="#E7E0D6", font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.07, rely=0.23)
            self.loginUserentry = Entry(self.AddCoffeeWindow, textvariable="procategory_var", font=("century gothic", 13), relief='ridge', bd=2)
            self.loginUserentry.place(relx=0.07, rely=0.28, relwidth=0.25, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Availability", bg="#27150C", fg="#E7E0D6", font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.07, rely=0.36)
            self.loginUserentry = Entry(self.AddCoffeeWindow, textvariable="proavaliablity_var", font=("century gothic", 13), relief='ridge', bd=2)
            self.loginUserentry.place(relx=0.07, rely=0.41, relwidth=0.25, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Price", bg="#27150C", fg="#E7E0D6", font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.4, rely=0.1)
            self.loginUserentry = Entry(self.AddCoffeeWindow, textvariable="proprice_var", font=("century gothic", 13), relief='ridge', bd=2)
            self.loginUserentry.place(relx=0.4, rely=0.15, relwidth=0.25, relheight=0.05)

            self.AddHeadLabel = Label(self.AddCoffeeWindow, text="Product Image", bg="#27150C", fg="#E7E0D6", font=("century gothic bold", 16))
            self.AddHeadLabel.place(relx=0.4, rely=0.23)
            self.loginUserentry = Entry(self.AddCoffeeWindow, textvariable="proimg_var", font=("century gothic", 13), relief='ridge', bd=2)
            self.loginUserentry.place(relx=0.4, rely=0.28, relwidth=0.25, relheight=0.05)

            self.AddProductButton = Button(self.AddCoffeeWindow, text="Add Product", background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, font=("century gothic bold", 12))
            self.AddProductButton.place(relx=0.73, rely=0.12, relwidth=0.2, relheight=0.08)

            self.EditProductButton = Button(self.AddCoffeeWindow, text="Edit Product", background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, font=("century gothic bold", 12))
            self.EditProductButton.place(relx=0.73, rely=0.24, relwidth=0.2, relheight=0.08)

            self.DeleteProductButton = Button(self.AddCoffeeWindow, text="Delete Product", background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, font=("century gothic bold", 12))
            self.DeleteProductButton.place(relx=0.73, rely=0.36, relwidth=0.2, relheight=0.08)

       




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






































