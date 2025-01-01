
# Database connection function
def db_connect():
    return mysql.connector.connect(
        host="localhost", user="root", password="password", database="your_database"
    )

# Check user credentials in the database
def check_credentials(username, password):
    db = db_connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

# Admin Dashboard class
class AdminDashboard():
    def __init__(self, window):
        self.window = window
        self.window.title("CAFEVIA")
        self.window.state('zoomed')  # Fullscreen
        self.window.resizable(False, False)
        self.window.config(background=secondary_color)

        # Add your admin dashboard content here
        welcome_label = Label(self.window, text="Welcome to CAFEVIA Dashboard!", font=("century gothic", 30), bg=secondary_color, fg=primary_color)
        welcome_label.pack(pady=20)

        # Additional dashboard elements can go here

# Login class
class Login():
    def __init__(self, loginwindow):
        self.loginwindow = loginwindow
        self.loginwindow.title("LOGIN - CAFEVIA")
        self.loginwindow.geometry('1000x600+200+100')
        self.loginwindow.resizable(False, False)
        self.loginwindow.config(background=secondary_color)

        # Login Image
        loginimage = Image.open('images/login_img.jpg')
        loginimage = ImageTk.PhotoImage(loginimage)
        loginimage_label = Label(self.loginwindow, image=loginimage,  background=secondary_color)
        loginimage_label.image = loginimage
        loginimage_label.place(relx=0, rely=0, relwidth=0.57, relheight=1)

        # User input fields
        self.name_var = StringVar()
        self.passw_var = StringVar()

        loginform = Frame(self.loginwindow, background=secondary_color)
        loginform.place(relx=0.37, rely=0, relwidth=0.63, relheight=1)

        closebutton = Button(loginform, text="x", font=("century gothic bold", 13), background=primary_color, 
                             foreground=secondary_color, cursor="hand2", relief="flat", activebackground=active_color, 
                             bd=2, command=self.close_window)
        closebutton.place(relx=0.94, rely=0.014, width=30, height=30)

        loginlogo = Label(loginform, text="CAFEVIA", bg=secondary_color, fg=primary_color, font=("century gothic bold", 30))
        loginlogo.place(relx=0.35, rely=0.07)

        # Username & Password labels and entry
        Label(loginform, text="Username", bg=secondary_color, fg=primary_color, font=("century gothic bold", 16)).place(relx=0.2, rely=0.3)
        Entry(loginform, textvariable=self.name_var, font=("century gothic", 13), relief='ridge', bd=2).place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.065)

        Label(loginform, text="Password", bg=secondary_color, fg=primary_color, font=("century gothic bold", 16)).place(relx=0.2, rely=0.46)
        Entry(loginform, textvariable=self.passw_var, font=("century gothic", 13), relief='ridge', bd=2, show='*').place(relx=0.2, rely=0.51, relwidth=0.6, relheight=0.065)

        login_button = Button(loginform, text="Login", font=("century gothic bold", 15), background=primary_color, 
                              foreground=secondary_color, cursor="hand2", relief="flat", bd=2, command=self.submit)
        login_button.place(relx=0.2, rely=0.68, relwidth=0.6, relheight=0.065)

        Label(loginform, text="Must check USERNAME & PASSWORD", bg=secondary_color, fg=primary_color, font=("century gothic", 8)).place(relx=0.2, rely=0.755, relwidth=0.6, relheight=0.015)

    def close_window(self):
        self.loginwindow.destroy()

    def submit(self):
        username = self.name_var.get()
        password = self.passw_var.get()

        if check_credentials(username, password):
            self.loginwindow.destroy()
            self.show_main_window()
        else:
            error_label = Label(self.loginwindow, text="Invalid username or password", bg=secondary_color, fg="red", font=("century gothic", 12))
            error_label.place(relx=0.5, rely=0.9, anchor="center")

    def show_main_window(self):
        main_window = Toplevel(self.loginwindow)
        AdminDashboard(main_window)  # Open Admin Dashboard
        main_window.mainloop()  # Start the new window's mainloop


