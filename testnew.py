from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

primary_color = "#FF5733"
secondary_color = "#2E2E2E"
active_color = "#FF784F"

class Login():
    def __init__(self, loginwindow):
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

        loginimage = Image.open('images/login_img.jpg')  # Replace with your image path
        loginimage = ImageTk.PhotoImage(loginimage)
        loginimage_label = Label(self.loginwindow, image=loginimage, background=secondary_color)
        loginimage_label.image = loginimage
        loginimage_label.place(relx=0, rely=0, relwidth=0.57, relheight=1)

        # Use Verification
        self.name_var = StringVar()
        self.passw_var = StringVar()

        loginform = Frame(loginwindow, background=secondary_color)
        loginform.place(relx=0.37, rely=0, relwidth=0.63, relheight=1)

        loginwindow.overrideredirect(True)

        def close_button():
            loginwindow.destroy() 
        closebutton = Button(loginform, text="x", font=("century gothic bold", 13), background=primary_color, 
                             foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, bd=2, command=close_button)
        closebutton.place(relx=0.94, rely=0.014, width=30, height=30)
        
        # login logo
        loginlogo = Label(loginform, text="CAFEVIA", bg=secondary_color, fg=primary_color, 
                          font=("century gothic bold", 30), bd=0)
        loginlogo.place(relx=0.35, rely=0.07)
        loginslogan = Label(loginform, text="Wake up, sip, and conquer your day with our brew.", 
                            bg=secondary_color, fg=primary_color, font=("century gothic", 10))
        loginslogan.place(relx=0.23, rely=0.15)

        loginUserlabel = Label(loginform, text="Username", bg=secondary_color, fg=primary_color, 
                               font=("century gothic bold", 16))
        loginUserlabel.place(relx=0.2, rely=0.3)
        txtProductName = Entry(loginform, textvariable=self.name_var, font=("century gothic", 13), relief='ridge', bd=2)
        txtProductName.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.065)

        loginPasswordlabel = Label(loginform, text="Password", bg=secondary_color, fg=primary_color, 
                                   font=("century gothic bold", 16))
        loginPasswordlabel.place(relx=0.2, rely=0.46)
        loginPasswordentry = Entry(loginform, textvariable=self.passw_var, font=("century gothic", 13), relief='ridge', 
                                   bd=2, show='*')
        loginPasswordentry.place(relx=0.2, rely=0.51, relwidth=0.6, relheight=0.065)

        login = Button(loginform, text="Login", font=("century gothic bold", 15), background=primary_color, 
                       foreground=secondary_color, cursor="hand2", relief="flat", bd=2, command=self.submit)
        login.place(relx=0.2, rely=0.68, relwidth=0.6, relheight=0.065)

        loginNote = Label(loginform, text="Must do check USERNAME & PASSWORD is correct", bg=secondary_color, 
                          fg=primary_color, font=("century gothic", 8))
        loginNote.place(relx=0.2, rely=0.755, relwidth=0.6, relheight=0.015)

    def submit(self):
        # For demo purposes, using hardcoded username and password
        if self.name_var.get() == "admin" and self.passw_var.get() == "password123":
            self.loginwindow.destroy()
            win()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

class AdminDashboard():
    def __init__(self, window):
        self.window = window
        self.window.title("CAFEVIA")
        self.window.state('zoomed')
        self.window.resizable(False, False)
        self.window.config(background=secondary_color)

        # Sidebar
        self.sidebar = Frame(self.window, bg=primary_color)
        self.sidebar.place(relx=0, rely=0, relwidth=0.18, relheight=1)

        # Example content for the dashboard
        welcome_label = Label(self.window, text="Welcome to Admin Dashboard!", font=("century gothic bold", 24), bg=secondary_color, fg=primary_color)
        welcome_label.place(relx=0.4, rely=0.4)

def win():
    window = Tk()
    AdminDashboard(window)
    window.mainloop()

if __name__ == '__main__':
    loginwindow = Tk()
    Login(loginwindow)
    loginwindow.mainloop()
