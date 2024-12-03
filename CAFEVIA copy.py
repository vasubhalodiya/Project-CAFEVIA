from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
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

        self.loginback = Frame(loginwindow, background=secondary_color)
        self.loginback.place(relx=0, rely=0, relwidth=1, relheight=1)

        loginimage = Image.open('images/login_img.jpg')
        loginimage = ImageTk.PhotoImage(loginimage)
        loginimage_label = Label(self.loginback, image=loginimage,  background=secondary_color)
        loginimage_label.image = loginimage
        loginimage_label.place(relx=0, rely=0, relwidth=0.57, relheight=1)

        #Use Verification
        name_var = StringVar()
        passw_var = StringVar()

        self.loginform = Frame(loginwindow, background=secondary_color)
        self.loginform.place(relx=0.37, rely=0, relwidth=0.63, relheight=1)

        loginwindow.overrideredirect(True)
        def close_button():
            loginwindow.destroy() 
        self.closebutton = Button(self.loginform, text="x", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=close_button)
        self.closebutton.place(relx=0.94, rely=0.014, width=30, height=30)
        
        # login logo
        self.loginlogo = Label(self.loginform, text="CAFEVIA", bg=secondary_color, fg=primary_color, font=("century gothic bold", 30), bd=0)
        self.loginlogo.place(relx=0.35, rely=0.07)
        self.loginslogan = Label(self.loginform, text="Wake up, sip, and conquer your day with our brew.", bg=secondary_color, fg=primary_color, font=("century gothic", 10))
        self.loginslogan.place(relx=0.23, rely=0.15)

        self.loginUserlabel = Label(self.loginform, text="Username", bg=secondary_color, fg=primary_color, font=("century gothic bold", 16))
        self.loginUserlabel.place(relx=0.2, rely=0.3)
        self.loginUserentry = Entry(self.loginform, textvariable="name_var", font=("century gothic", 13), relief='ridge', bd=2)
        self.loginUserentry.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.065)

        self.loginPasswordlabel = Label(self.loginform, text="Password", bg=secondary_color, fg=primary_color, font=("century gothic bold", 16))
        self.loginPasswordlabel.place(relx=0.2, rely=0.46)
        self.loginPasswordentry = Entry(self.loginform, textvariable="passw_var", font=("century gothic", 13), relief='ridge', bd=2, show='*')
        self.loginPasswordentry.place(relx=0.2, rely=0.51, relwidth=0.6, relheight=0.065)

        self.login = Button(self.loginform, text="Login", font=("century gothic bold", 15), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", bd=2, command=submit)
        self.login.place(relx=0.2, rely=0.68, relwidth=0.6, relheight=0.065)
        self.loginNote = Label(self.loginform, text="Must do check USERNAME & PASSWORD is correct", bg=secondary_color, fg=primary_color, font=("century gothic", 8))
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
            
            self.MenuCartItem = Label(MenuCartFrame, text="Cart", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 20))
            self.MenuCartItem.place(relx=0.03, rely=0.01)

            self.MenuCartOrderNo = Label(MenuCartFrame, text="Order #3243", bg=sidecart_color, fg=primary_color, font=("century gothic", 10))
            self.MenuCartOrderNo.place(relx=0.7, rely=0.02)

            self.MenuCartDineInBtn = Button(MenuCartFrame, text="Dine In", font=("century gothic bold", 11), background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            self.MenuCartDineInBtn.place(relx=0.05, rely=0.07, relwidth=0.25, relheight=0.04)

            self.MenuCartTakeAwayBtn = Button(MenuCartFrame, text="Take away", font=("century gothic bold", 11), background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            self.MenuCartTakeAwayBtn.place(relx=0.35, rely=0.07, relwidth=0.35, relheight=0.04)

            self.MenuCartProductCardParent = Frame(MenuCartFrame, background=sidecart_color)
            self.MenuCartProductCardParent.place(relx=0.05, rely=0.16, relwidth=0.91, relheight=0.11)

            MenuCartProductImage = Image.open('images/coffee.png').resize((60, 60))
            MenuCartProductImage = ImageTk.PhotoImage(MenuCartProductImage)
            MenuCartProductImage_label = Label(self.MenuCartProductCardParent, image=MenuCartProductImage, background=sidecart_color)
            MenuCartProductImage_label.image = MenuCartProductImage
            MenuCartProductImage_label.place(relx=0, rely=0.09, width=75, height=75)

            self.MenuCartProductName = Label(self.MenuCartProductCardParent, text="Hello World Coffee", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13))
            self.MenuCartProductName.place(relx=0.3, rely=0.1)

            self.MenuCartOrderPrice = Label(self.MenuCartProductCardParent, text="₹ 100", bg=price_color, fg=secondary_color, font=("century gothic bold", 13))
            self.MenuCartOrderPrice.place(relx=0.32, rely=0.5, relwidth=0.21, relheight=0.24)

            self.MenuCartMinusBtn = Button(self.MenuCartProductCardParent, text="-", font=("century gothic bold", 15), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            self.MenuCartMinusBtn.place(relx=0.6, rely=0.5, width=25, height=25)
            # *************
            self.MenuCartItemNo = Label(self.MenuCartProductCardParent, text="3", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 15))
            self.MenuCartItemNo.place(relx=0.7, rely=0.5, width=22, height=22)
            # *************
            self.MenuCartPlusBtn = Button(self.MenuCartProductCardParent, text="+", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            self.MenuCartPlusBtn.place(relx=0.8, rely=0.5, width=25, height=25)
        # ===================================================
            self.MenuCartProductCardParent = Frame(MenuCartFrame, background=sidecart_color)
            self.MenuCartProductCardParent.place(relx=0.05, rely=0.3, relwidth=0.91, relheight=0.11)

            MenuCartProductImage = Image.open('images/coffee.png').resize((60, 60))
            MenuCartProductImage = ImageTk.PhotoImage(MenuCartProductImage)
            MenuCartProductImage_label = Label(self.MenuCartProductCardParent, image=MenuCartProductImage, background=sidecart_color)
            MenuCartProductImage_label.image = MenuCartProductImage
            MenuCartProductImage_label.place(relx=0, rely=0.09, width=75, height=75)

            self.MenuCartProductName = Label(self.MenuCartProductCardParent, text="Hello World Coffee", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 13))
            self.MenuCartProductName.place(relx=0.3, rely=0.1)

            self.MenuCartOrderPrice = Label(self.MenuCartProductCardParent, text="₹ 100", bg=price_color, fg=secondary_color, font=("century gothic bold", 13))
            self.MenuCartOrderPrice.place(relx=0.32, rely=0.5, relwidth=0.21, relheight=0.24)

            self.MenuCartMinusBtn = Button(self.MenuCartProductCardParent, text="-", font=("century gothic bold", 15), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            self.MenuCartMinusBtn.place(relx=0.6, rely=0.5, width=25, height=25)
            # *************
            self.MenuCartItemNo = Label(self.MenuCartProductCardParent, text="3", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 15))
            self.MenuCartItemNo.place(relx=0.7, rely=0.5, width=22, height=22)
            # *************
            self.MenuCartPlusBtn = Button(self.MenuCartProductCardParent, text="+", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            self.MenuCartPlusBtn.place(relx=0.8, rely=0.5, width=25, height=25)
        # ===================================================

            self.MenuCartItemTotal = Label(MenuCartFrame, text="Items", bg=sidecart_color, fg=primary_color, font=("century gothic", 11), anchor="w")
            self.MenuCartItemTotal.place(relx=0.05, rely=0.77, relwidth=0.2, relheight=0.03)
            self.MenuCartItemTotalAns = Label(MenuCartFrame, text="₹ 1000", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 12), anchor="e")
            self.MenuCartItemTotalAns.place(relx=0.7, rely=0.77, relwidth=0.25, relheight=0.03)
            # *************
            self.MenuCartDiscountTotal = Label(MenuCartFrame, text="Discount", bg=sidecart_color, fg=primary_color, font=("century gothic", 11), anchor="w")
            self.MenuCartDiscountTotal.place(relx=0.05, rely=0.81, relwidth=0.25, relheight=0.03)
            self.MenuCartDiscountTotalAns = Label(MenuCartFrame, text="- ₹100", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 12), anchor="e")
            self.MenuCartDiscountTotalAns.place(relx=0.75, rely=0.81, relwidth=0.2, relheight=0.03)

            # *************
            self.MenuCartTotalFrame = Frame(MenuCartFrame, background=sidecart_color)
            self.MenuCartTotalFrame.place(relx=0.05, rely=0.86, relwidth=0.9, relheight=0.14)
            top_border = Frame(self.MenuCartTotalFrame, bg="#CBA084", height=1)
            top_border.pack(side="top", fill="x")
            # *************
            self.MenuCartAllTotal = Label(self.MenuCartTotalFrame, text="Total", bg=sidecart_color, fg=primary_color, font=("century gothic bold", 12), anchor="w")
            self.MenuCartAllTotal.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.2)
            self.MenuCartAllTotalAns = Label(self.MenuCartTotalFrame, text="₹ 1000", bg=price_color, fg=secondary_color, font=("century gothic bold", 12))
            self.MenuCartAllTotalAns.place(relx=0.73, rely=0.2, relwidth=0.28, relheight=0.2)
            # *************
            self.MenuCartPlaceOrderBtn = Button(self.MenuCartTotalFrame, text="Place an order", font=("century gothic bold", 13), background=primary_color, foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2)
            self.MenuCartPlaceOrderBtn.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)



        # ================== Menu Cart Product End=====================

            self.ChooseCategory = Label(MenuFrame, text="Choose Category", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            self.ChooseCategory.place(relx=0.03, rely=0.02)

            # ============================
            # categoryimage = Image.open('images/all.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="All", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.03, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/coffee.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Coffee", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.16, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/softdrink.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Softdrink", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.29, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/pizza.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Pizza", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.42, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/burger.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Burger", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.55, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/dessert.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Dessert", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
            # self.CategoryChildCard.place(relx=0.68, rely=0.08, width=110, height=110)
            # # ============================
            # categoryimage = Image.open('images/meal.png').resize((45, 45))
            # categoryimage = ImageTk.PhotoImage(categoryimage)
            # categoryimage_label = Label(MenuFrame, image=categoryimage, background=sidecart_color)
            # categoryimage_label.image = categoryimage
            # self.CategoryChildCard = Button(MenuFrame, text="Food Meal", background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, image=categoryimage, compound="top", font=("century gothic bold", 12), pady=13)
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
                
                self.CategoryChildCard = Button(MenuFrame, text=category["name"], image=category_image, background=sidecart_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, compound="top", font=("century gothic bold", 12), pady=13)
                self.CategoryChildCard.image = category_image
                self.CategoryChildCard.place(relx=relx, rely=0.08, width=110, height=110)
           
# =============================================================================================

            self.CoffeeCategory = Frame(MenuFrame, background=secondary_color)
            self.CoffeeCategory.place(relx=0, rely=0.27, relwidth=0.95, relheight=1)
            self.CoffeeCategoryLabel = Label(self.CoffeeCategory, text="Coffee Menu", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            self.CoffeeCategoryLabel.place(relx=0.03, rely=0.02)

    # ================= add coffee button =======================

            self.AddCoffeeButton = Button(self.CoffeeCategory, text="Add New Dish to \nCoffee", background=sidecart_color, cursor="hand2", relief="solid", activebackground=active_color, bd=1, compound="top", font=("century gothic bold", 12), pady=20, command=MovieCRUD_calling)
            self.AddCoffeeButton.place(relx=0.03, rely=0.08, relwidth=0.21, relheight=0.25)

          

# =========================================================================================================


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

class MovieCRUD:
    def _init_(self,MovieCRUDwindow):
        self.MovieCRUDwindow = MovieCRUDwindow
        self.MovieCRUDwindow.title("BOOK MY SHOW - ADD UPDATE DELETE MOVIE")
        self.MovieCRUDwindow.geometry("1000x600")
        self.MovieCRUDwindow.state('normal')

        # #Variable Declaration
        # id_int = int()
        # MovieName = StringVar()
        # ReleaseDate = StringVar()
        # category = StringVar()
        # Duration = StringVar()
        # Language = StringVar()
        # Short_Description = StringVar()
        # Formatee = StringVar()

        # # CRUD OPERATION FUNCTION
        # # INSERT function
        # def Movieinsert():
        #     MovieId = txtid.get()
        #     MovieName = txtMovieName.get()
        #     ReleaseDate = txtReleaseDate.get()

        #     MovieCategory = txtMovieCategory.get()
        #     MovieDuration = txtMovieDuration.get()
        #     MovieLanguage = txtMovieLanguage.get()

        #     ShortDescription = txtShortDescription.get()
        #     MovieFormate = txtMovieFormate.get()

        #     if(MovieId=="" or MovieName=="" or ReleaseDate=="" or MovieCategory=="" or MovieDuration=="" or MovieLanguage=="" or ShortDescription=="" or MovieFormate==""):
        #         messagebox.showinfo("Insert Status","All fields are required")
        #     else:
        #         con = MySQLdb.connect(host="localhost", user="root", password="", database="bookmyshow")
        #         cursor = con.cursor()
        #         cursor.execute("insert into movie_details values('"+MovieId+"','"+MovieName+"','"+ReleaseDate+"','"+MovieCategory+"','"+MovieDuration+"','"+MovieLanguage+"','"+ShortDescription+"','"+MovieFormate+"')")
        #         cursor.execute("commit")

        #         txtid.delete(0,'end')
        #         txtMovieName.delete(0,'end')
        #         txtReleaseDate.delete(0,'end')

        #         txtMovieCategory.delete(0,'end')
        #         txtMovieDuration.delete(0,'end')
        #         txtMovieLanguage.delete(0,'end')

        #         txtShortDescription.delete(0,'end')
        #         txtMovieFormate.delete(0,'end')
        #         messagebox.showinfo("INSERT Status","INSERTED SUCCESSFULLY")
        #         con.close()

        # # ALL FIELD's AND FRAME
        # CRUDtxtFild = Frame(MovieCRUDwindow,background='#800808')
        # CRUDtxtFild.config(height=350,width=1000)
        # CRUDtxtFild.place(x=0,y=0)

        # CRUDmenu = Frame(CRUDtxtFild,background='white')
        # CRUDmenu.config(height=30,width=1000)
        # CRUDmenu.place(x=0,y=10)

        # MovieAddBtn = Button(CRUDmenu,text="ADD MOVIE",font=("century gothic bold",10),width=15,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=Movieinsert)
        # MovieAddBtn.place(x=540,y=0)

        # MoviewDetails = Label(CRUDmenu,text="  MOVIE DETAIL's  ",font=('century gothic bold',20),background='#880808',foreground='white')
        # MoviewDetails.place(x=50,y=0)

        # lblid = Label(CRUDtxtFild,text="MOVIE ID :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblid.place(x=50,y=70)

        # txtid = Entry(CRUDtxtFild,textvariable=id_int,font=('century gothic',15),width=20,relief='ridge')
        # txtid.place(x=50,y=100)

        # lblMovieName = Label(CRUDtxtFild,text="MOVIE NAME :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieName.place(x=50,y=150)

        # txtMovieName = Entry(CRUDtxtFild,textvariable=MovieName,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieName.place(x=50,y=180)

        # lblReleaseDate = Label(CRUDtxtFild,text="RELEASE DATE :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblReleaseDate.place(x=50,y=230)

        # txtReleaseDate = Entry(CRUDtxtFild,textvariable=ReleaseDate,font=('century gothic',15),width=20,relief='ridge')
        # txtReleaseDate.place(x=50,y=260)

        # lblMovieCategory = Label(CRUDtxtFild,text="MOVIE CATEGORY :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieCategory.place(x=390,y=70)
        
        # txtMovieCategory = Entry(CRUDtxtFild,textvariable=category,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieCategory.place(x=390,y=100)

        # lblMovieDuration = Label(CRUDtxtFild,text="MOVIE DURATION :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieDuration.place(x=390,y=150)
        
        # txtMovieDuration = Entry(CRUDtxtFild,textvariable=Duration,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieDuration.place(x=390,y=180)

        # lblMovieLanguage = Label(CRUDtxtFild,text="MOVIE LANGUAGE :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieLanguage.place(x=390,y=230)

        # txtMovieLanguage = Entry(CRUDtxtFild,textvariable=Language,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieLanguage.place(x=390,y=260)

        # lblShortDescription = Label(CRUDtxtFild,text="SHORT DESCRIPTION :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblShortDescription.place(x=730,y=70)
        
        # txtShortDescription = Entry(CRUDtxtFild,textvariable=Short_Description,font=('century gothic',15),width=20,relief='ridge')
        # txtShortDescription.place(x=730,y=100)

        # lblMovieimage = Label(CRUDtxtFild,text="MOVIE IMAGE :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieimage.place(x=730,y=150)
        
        # txtMovieimage = Entry(CRUDtxtFild,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieimage.place(x=730,y=180)

        # lblMovieFormat = Label(CRUDtxtFild,text="MOVIE FORMATE :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieFormat.place(x=730,y=230)

        # txtMovieFormate = Entry(CRUDtxtFild,textvariable=Formatee,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieFormate.place(x=730,y=260)

        # #DATAGRID VIEW AND DATA DESIGN       MovieCRUDwindow
        # CRUDtxtDatagridView = Frame(MovieCRUDwindow,background='black')
        # CRUDtxtDatagridView.config(height=350,width=1000)
        # CRUDtxtDatagridView.place(x=0,y=350)




def MovieCRUD_calling():
    MovieCRUDwindow = Tk()
    MovieCRUD(MovieCRUDwindow)
    MovieCRUDwindow.mainloop()

def win():
    window = Tk()
    AdminDashboard(window)
    window.mainloop()

if __name__ == '__main__':

    # loginwindow = Tk()
    # Login(loginwindow)
    # loginwindow.mainloop()
    win()






































