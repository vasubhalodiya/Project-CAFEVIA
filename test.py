from tkinter import *
from PIL import ImageTk, Image

class Login():
    def _init_(self,loginwindow):
        self.loginwindow = loginwindow
        self.loginwindow.title("It's Time To Work")
        self.loginwindow.geometry("650x400")
        self.loginwindow.state('normal')
        self.loginwindow.config(background='#fffbda')

        # Login Image
        image = Image.open('image/logo.png')
        image = ImageTk.PhotoImage(image)
        image_label = Label(loginwindow, image=image, height=100, width=100, background='#fffbda')
        image_label.image = image
        image_label.place(x=150, y=150)

class AdminDashboard():

    def _init_(self,window):
        self.window = window
        self.window.title("Bank Management System")
        self.window.geometry("1500x750")
        self.window.state('zoomed')
        self.window.config(background='#fffbda')

        # header
        self.header = Frame(self.window, bg='#730000')
        self.header.place(x=225, y=0, height=40, width=1320)

        self.headertext = Label(self.window, text='Bank Management System', foreground='white', background='#730000', font=("century gothic bold",12), width=23, height=1)
        self.headertext.place(x=270, y=5)

        self.versiontext = Label(self.window, text='Version 1.0', foreground='white', background='#730000', font=("century gothic bold",8), width=8, height=1)
        self.versiontext.place(x=485, y=8)

        # sidebar
        self.sidebar = Frame(self.window, bg='#730000')
        self.sidebar.place(x=0, y=0, height=850, width=225) 

        logoimage = Image.open('image/logo.png')
        logoimage = ImageTk.PhotoImage(logoimage)
        logoimage_label = Label(window, image=logoimage, height=100, width=100, background='#fffbda')
        logoimage_label.image = logoimage
        logoimage_label.place(x=150, y=150)

        DashboardButton = Button(self.sidebar,text="Dashboard",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3, command= lambda:MenuSystem(DashboardMenu))
        DashboardButton.place(x=0, y=250)
        
        CustomerButton = Button(self.sidebar,text="Customer Account Management",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3, command= lambda:MenuSystem(CustomerMenu))
        CustomerButton.place(x=0, y=300)
    
        AccountManageButton = Button(self.sidebar,text="Account Management",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3, command= lambda:MenuSystem(AccountMenu))
        AccountManageButton.place(x=0, y=350)
        
        TransactionManageButton = Button(self.sidebar,text="Transaction Management",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3, command= lambda:MenuSystem(TransactionMenu))
        TransactionManageButton.place(x=0, y=400)
        
        LoanButton = Button(self.sidebar,text="Loan Management",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3, command= lambda:MenuSystem(LoanMenu))
        LoanButton.place(x=0, y=450)
    
        ReportGenerationButton = Button(self.sidebar,text="Report Generation",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3, command= lambda:MenuSystem(ReportMenu))
        ReportGenerationButton.place(x=0, y=500)

        SecurityAndAuditButton = Button(self.sidebar,text="Security And Audit",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3, command= lambda:MenuSystem(SecurityMenu))
        SecurityAndAuditButton.place(x=0, y=550)

        DataManagementButton = Button(self.sidebar,text="Data Management",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3, command= lambda:MenuSystem(DataMenu))
        DataManagementButton.place(x=0, y=600)

        SettingsButton = Button(self.sidebar,text="Settings",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3, command= lambda:MenuSystem(SettingMenu))
        SettingsButton.place(x=0, y=650)

        LogoutButton = Button(self.sidebar,text="LogOut",font=("century gothic bold",10), width=27, height=1,background="darkred", foreground="white", cursor="hand2", highlightthickness=2, relief="flat", overrelief="raised", activebackground="darkorange", bd=3)
        LogoutButton.place(x=0, y=750)

        # Functionality for menu system
        main_frame = Frame(window)
        main_frame.config( background='#fffbda', height=760, width=1311)
        main_frame.place(x=225, y=40)

        def MenuSystem(page):
            for frame in main_frame.winfo_children():
                frame.destroy()
            page()


        def DashboardMenu():
            dashboardFrame = Frame(main_frame, background='orange')
            dashboardFrame.config(height=760, width=1310)
            dashboardFrame.place(x=0, y=0)

        def CustomerMenu():
            CustomerFrame = Frame(main_frame, background='#fffbda')
            CustomerFrame.config(height=760, width=1310)
            CustomerFrame.place(x=0, y=0)

        def AccountMenu():
            AccountFrame = Frame(main_frame, background='red')
            AccountFrame.config(height=760, width=1310)
            AccountFrame.place(x=0, y=0)

        def TransactionMenu():
            TransactionFrame = Frame(main_frame, background='#fffbda')
            TransactionFrame.config(height=760, width=1310)
            TransactionFrame.place(x=0, y=0)

        def LoanMenu():
            LoanFrame = Frame(main_frame, background='yellow')
            LoanFrame.config(height=760, width=1310)
            LoanFrame.place(x=0, y=0)

        def ReportMenu():
            ReportFrame = Frame(main_frame, background='#fffbda')
            ReportFrame.config(height=760, width=1310)
            ReportFrame.place(x=0, y=0)

        def SecurityMenu():
            SecurityFrame = Frame(main_frame, background='white')
            SecurityFrame.config(height=760, width=1310)
            SecurityFrame.place(x=0, y=0)

        def DataMenu():
            DataFrame = Frame(main_frame, background='black')
            DataFrame.config(height=760, width=1310)
            DataFrame.place(x=0, y=0)

        def SettingMenu():
            SettingFrame = Frame(main_frame, background='#fffbda')
            SettingFrame.config(height=760, width=1310)
            SettingFrame.place(x=0, y=0)

        # def LogoutMenu():
        #     LogoutFrame = Frame(main_frame, background='red')
        #     LogoutFrame.config(height=760, width=1310)
        #     LogoutFrame.place(x=225, y=40)



def win():
    window = Tk()
    AdminDashboard(window)
    window.mainloop()

if __name__ == '__main__':

    # loginwindow = Tk()
    # Login(loginwindow)
    # loginwindow.mainloop()
    win()