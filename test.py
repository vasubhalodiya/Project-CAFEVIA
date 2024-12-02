import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image

class LoadingScreen:
    def __init__(self):
        self.window = tk.Tk()
        width = 370
        height = 230
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
        self.window.overrideredirect(True)
        self.window.configure(bg="#E7E0D6")

        loading_text = tk.Label(self.window, text="CAFEVIA", font=("Century Gothic", 30, "bold"), bg="#E7E0D6", fg="#27150C")
        loading_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.window.after(3000, self.redirect_to_home)
        self.window.mainloop()

    def redirect_to_home(self):
        self.window.destroy()
        AdminDashboard()

class Login:
    def __init__(self):
        self.loginwindow = tk.Tk()
        self.loginwindow.title("LOGIN - CAFEVIA")
        width = 1000
        height = 600
        x = (self.loginwindow.winfo_screenwidth() // 2) - (width // 2)
        y = (self.loginwindow.winfo_screenheight() // 2) - (height // 2)
        self.loginwindow.geometry(f'{width}x{height}+{x}+{y}')
        self.loginwindow.state('normal')
        self.loginwindow.resizable(False, False)
        self.loginwindow.config(background='#E7E0D6')

        # ... (rest of the Login class code)

class AdminDashboard:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("CAFEVIA")
        self.window.state('zoomed')
        self.window.resizable(False, False)
        self.window.config(background='#E7E0D6')

        # Sidebar
        self.sidebar = tk.Frame(self.window, bg='#27150C')
        self.sidebar.place(relx=0, rely=0, relwidth=0.18, relheight=1)

        # ... (rest of the AdminDashboard class code)

    def menu_system(self, page):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
        page()

    def dashboard_menu(self):
        dashboard_frame = tk.Frame(self.main_frame, background='red')
        dashboard_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # ... (other menu methods)

    def add_coffee_product(self):
        add_coffee_window = tk.Toplevel(self.window)
        add_coffee_window.title("Add Coffee - CAFEVIA")
        width = 1200
        height = 750
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        add_coffee_window.geometry(f'{width}x{height}+{x}+{y}')
        add_coffee_window.resizable(False, False)
        add_coffee_window.config(background='#E7E0D6')

        # ... (rest of the add_coffee_product method)

def main():
    loading_screen = LoadingScreen()
    # The AdminDashboard will be created after the loading screen closes

if __name__ == '__main__':
    main()

# Simulating print output for demonstration
print("Cafe Management System initialized.")
print("Loading screen displayed for 3 seconds.")
print("Admin Dashboard opened.")