from tkinter import *
from PIL import ImageTk, Image
# from tkinter import ttk, messagebox
# import MySQLdb
import MySQLdb
from tkinter import messagebox

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

            AddProductButton = Button(CoffeeCategory, text="Add Product", background=primary_color, foreground=secondary_color, cursor="hand2", relief="solid", activebackground=active_color, bd=0, font=("century gothic bold", 12), command=ProductMenu)
            AddProductButton.place(relx=0.815, rely=0.02, relwidth=0.15, relheight=0.05)

# =========================================================================================================

             # Add a scrollbar to the ProductCategorymain_frame
            ProductCategorymain_frame = Frame(CoffeeCategory)
            ProductCategorymain_frame.place(relx=0, rely=0.08, relwidth=1, relheight=0.66)

            # Create a Canvas inside the ProductCategorymain_frame
            Produc_canvas = Canvas(ProductCategorymain_frame, bg=secondary_color)
            Produc_canvas.pack(side="left", fill="both", expand=True)

            # Create a vertical scrollbar
            scrollbar = Scrollbar(ProductCategorymain_frame, orient="vertical", command=Produc_canvas.yview)
            # scrollbar.pack(side="right", fill="y")
            scrollbar.place(relx=0.988, rely=0, relwidth=0.013, relheight=1)

            # Configure the canvas to use the scrollbar
            Produc_canvas.configure(yscrollcommand=scrollbar.set)

            # Create a frame inside the canvas to hold the content
            canvas_frame = Frame(Produc_canvas, background=secondary_color)
            Produc_canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

            # Bind the canvas to resize the scroll region
            def update_scrollregion(event):
                Produc_canvas.configure(scrollregion=Produc_canvas.bbox("all"))

            canvas_frame.bind("<Configure>", update_scrollregion)

            # Add mousewheel scrolling functionality
            def on_mousewheel(event):
                Produc_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

            Produc_canvas.bind_all("<MouseWheel>", on_mousewheel)

            # Function to fetch and display products
            def fetch_and_display_products():
                # Clear existing product cards
                for widget in canvas_frame.winfo_children():
                    widget.destroy()

                # Fetch updated product list from the database
                con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM product")
                products = cursor.fetchall()
                con.close()

                # Display the products
                row_frame = None
                card_count = 0
                for product_details in products:
                    if card_count % 4 == 0:
                        row_frame = Frame(canvas_frame, background=secondary_color)
                        row_frame.pack(padx=20, pady=10)

                    ProductDtlCard = Frame(row_frame, background=sidecart_color, width=200, height=210)
                    ProductDtlCard.grid(row=0, column=card_count % 4, padx=15)

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

            # Function to add a product and refresh the UI
            def add_product_to_database(product_name, category, price):
                con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                cursor = con.cursor()
                cursor.execute("INSERT INTO product (name, category, price) VALUES (%s, %s, %s)", (product_name, category, price))
                con.commit()
                con.close()

                # Refresh the product list after insertion
                fetch_and_display_products()

            # Fetch and display products initially
            fetch_and_display_products()

            # Example: Call this function after adding a product
            # add_product_to_database('New Coffee', 'Beverage', 150)



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
            AddCoffeeWindow.attributes("-topmost", True)

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

            def ProductDelete():
                if(txtProductId.get() == ""):
                    messagebox.showinfo("Delete Status", "ID is required for delete operation")
                else:
                    try:
                        # Connect to the database
                        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                        cursor = con.cursor()

                        # query = "DELETE FROM product WHERE proid = %s"
                        cursor.execute("delete from product where proid='"+txtProductId.get()+"'")
                        con.commit()

                        txtProductId.delete(0, 'end')
                        txtProductName.delete(0, 'end')
                        txtProductCategory.delete(0, 'end')
                        txtProductAvaliable.delete(0, 'end')
                        txtProductPrice.delete(0, 'end')
                        txtProductImage.delete(0, 'end')

                        messagebox.showinfo("DELETE Status", "Deleted Successfully")
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred: {str(e)}")
                    con.close()

            def ProductUpdate():
                ProductId = txtProductId.get()
                ProductName = txtProductName.get()
                ProductCategory = txtProductCategory.get()
                ProductAvaliable = txtProductAvaliable.get()
                ProductPrice = txtProductPrice.get()
                ProductImage = txtProductImage.get()

                if (ProductId=="" or ProductName=="" or ProductCategory=="" or ProductAvaliable=="" or ProductPrice=="" or ProductImage==""):
                    messagebox.showinfo("Update Status", "All fields are required")
                else:
                    try:
                        # Connect to the database
                        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
                        cursor = con.cursor()

                        cursor.execute("update product set proname='"+txtProductName.get()+"',procategory='"+txtProductCategory.get()+"',proavailable='"+txtProductAvaliable.get()+"',proprice='"+txtProductPrice.get()+"',proimage='"+txtProductImage.get()+"' where proid='"+txtProductId.get()+"'")
                        con.commit()

                        # Clear input fields
                        txtProductId.delete(0, 'end')
                        txtProductName.delete(0, 'end')
                        txtProductCategory.delete(0, 'end')
                        txtProductAvaliable.delete(0, 'end')
                        txtProductPrice.delete(0, 'end')
                        txtProductImage.delete(0, 'end')
                        messagebox.showinfo("UPDATE Status", "UPDATED SUCCESSFULLY")

                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred: {str(e)}")
                    con.close()



            AddNavbar = Frame(AddCoffeeWindow, background=primary_color)
            AddNavbar.place(relx=0, rely=0, relwidth=1, relheight=0.5)

            AddHeadLabel = Label(AddCoffeeWindow, text="Add Coffee", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
            AddHeadLabel.place(relx=0, rely=0.02, relwidth=1, relheight=0.05)

            lblProductId = Label(AddCoffeeWindow, text="Product Id", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductId.place(relx=0.07, rely=0.1)
            txtProductId = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductId.place(relx=0.07, rely=0.15, relwidth=0.25, relheight=0.05)

            lblProductCategory = Label(AddCoffeeWindow, text="Product Category", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductCategory.place(relx=0.07, rely=0.23)
            txtProductCategory = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductCategory.place(relx=0.07, rely=0.28, relwidth=0.25, relheight=0.05)

            lblProductAvaliable = Label(AddCoffeeWindow, text="Product Availability", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductAvaliable.place(relx=0.07, rely=0.36)
            txtProductAvaliable = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductAvaliable.place(relx=0.07, rely=0.41, relwidth=0.25, relheight=0.05)

            lblProductName = Label(AddCoffeeWindow, text="Product Name", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductName.place(relx=0.4, rely=0.1)
            txtProductName = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductName.place(relx=0.4, rely=0.15, relwidth=0.25, relheight=0.05)

            lblProductPrice = Label(AddCoffeeWindow, text="Product Price", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductPrice.place(relx=0.4, rely=0.23)
            txtProductPrice = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductPrice.place(relx=0.4, rely=0.28, relwidth=0.25, relheight=0.05)

            lblProductImage = Label(AddCoffeeWindow, text="Product Image", bg=primary_color, fg=secondary_color, font=("century gothic bold", 16))
            lblProductImage.place(relx=0.4, rely=0.36)
            txtProductImage = Entry(AddCoffeeWindow, font=("century gothic", 13), relief='ridge', bd=2)
            txtProductImage.place(relx=0.4, rely=0.41, relwidth=0.25, relheight=0.05)

            AddProductButton = Button(AddCoffeeWindow, text="Add Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=Productinsert)
            AddProductButton.place(relx=0.73, rely=0.12, relwidth=0.2, relheight=0.08)

            EditProductButton = Button(AddCoffeeWindow, text= "Edit Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=ProductUpdate)
            EditProductButton.place(relx=0.73, rely=0.24, relwidth=0.2, relheight=0.08)

            DeleteProductButton = Button(AddCoffeeWindow, text="Delete Product", background=secondary_color, foreground=primary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, font=("century gothic bold", 12), command=ProductDelete)
            DeleteProductButton.place(relx=0.73, rely=0.36, relwidth=0.2, relheight=0.08)


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






































