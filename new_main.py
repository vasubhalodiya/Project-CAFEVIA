from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

def loading_screen():
    window = Tk()
    width = 370
    height = 230
    x = (window.winfo_screenwidth()//2)-(width//2)
    y = (window.winfo_screenheight()//2)-(height//2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.overrideredirect(True)
    window.configure(bg="#E7E0D6")

    # text = "CAFEVIA"
    # spaced_text = " ".join(text)

    loading_text = Label(window, text="CAFEVIA", font=("century gothic bold", 30), bg="#E7E0D6", fg="#27150C")
    loading_text.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    def redirectToHome():
        window.destroy()
        AdminDashboard()

    window.after(3000, redirectToHome)
    window.mainloop()

loading_screen()

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

        self.login = Button(self.loginform, text="Login", font=("century gothic bold", 15), background="#27150C", foreground="#E7E0D6", cursor="hand2", relief="flat", bd=2, command=win)
        self.login.place(relx=0.2, rely=0.68, relwidth=0.6, relheight=0.065)
        self.loginNote = Label(self.loginform, text="Must do check USERNAME & PASSWORD is correct", bg="#E7E0D6", fg="#27150C", font=("century gothic", 8))
        self.loginNote.place(relx=0.2, rely=0.755, relwidth=0.6, relheight=0.015)

        def Submit(name, passv):
            mylabel = Label(self.loginform, text = name + passv).pack()



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

        # logoimage = Image.open('images/logo.jpg')
        # logoimage = ImageTk.PhotoImage(logoimage)
        # logoimage_label = Label(self.sidebar, image=logoimage, height=100, width=100, background='#27150C')
        # logoimage_label.image = logoimage
        # logoimage_label.place(relx=0.4, rely=0.05, width=100, height=100)

        DashboardButton = Button(self.sidebar, text="Dashboard", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(DashboardMenu))
        DashboardButton.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.05)

        OrderButton = Button(self.sidebar, text="Orders", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(OrderMenu))
        OrderButton.place(relx=0.1, rely=0.28, relwidth=0.8, relheight=0.05)

        BillingButton = Button(self.sidebar, text="Billing", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(BillingMenu))
        BillingButton.place(relx=0.1, rely=0.36, relwidth=0.8, relheight=0.05)

        TableBookButton = Button(self.sidebar, text="Table Book", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(TableBookMenu))
        TableBookButton.place(relx=0.1, rely=0.44, relwidth=0.8, relheight=0.05)

        SalesButton = Button(self.sidebar, text="Sales", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(SalesMenu))
        SalesButton.place(relx=0.1, rely=0.52, relwidth=0.8, relheight=0.05)

        LogoutButton = Button(self.sidebar, text="Logout", font=("century gothic bold", 11), width=27, height=1, background="#E7E0D6", foreground="#27150C", cursor="hand2", relief="flat", activebackground="#EDD6B3", bd=2, command=lambda:MenuSystem(LogoutMenu))
        LogoutButton.place(relx=0.1, rely=0.60, relwidth=0.8, relheight=0.05)

        # Functionality for menu system
        main_frame = Frame(window, background='#E7E0D6')
        main_frame.place(relx=0.18, rely=0, relwidth=0.82, relheight=1)

        def MenuSystem(page):
            for frame in main_frame.winfo_children():
                frame.destroy()
            page()

        def DashboardMenu():
            DashboardFrame = Frame(main_frame, background='red')
            DashboardFrame.place(relx=0, rely=0, relwidth=1, relheight=1)





        # ==========================================

        def OrderMenu():
            OrderFrame = Frame(main_frame, background='blue')
            OrderFrame.place(relx=0, rely=0, relwidth=1, relheight=1)





        # ==========================================

        def BillingMenu():
            BillingFrame = Frame(main_frame, background='green')
            BillingFrame.place(relx=0, rely=0, relwidth=1, relheight=1)




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
            # loginwindow = Tk()
            # Login(loginwindow)
            # loginwindow.mainloop()


















































def win():
    window = Tk()
    AdminDashboard(window)
    window.mainloop()
    # loginwindow = Tk()
    # Login(loginwindow)
    # loginwindow.mainloop()

if __name__ == '__main__':

    loginwindow = Tk()
    Login(loginwindow)
    loginwindow.mainloop()
    # win()






































