import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'auth_system'
}

# Initialize database connection
def init_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        ''')
        conn.commit()
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

class AuthApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Authentication System")
        self.geometry("300x200")
        self.db_conn = init_db()
        self.current_frame = None
        self.show_login_page()

    def show_login_page(self):
        self.clear_frame()
        LoginPage(self)

    def show_signup_page(self):
        self.clear_frame()
        SignupPage(self)

    def show_welcome_page(self, username):
        self.clear_frame()
        WelcomePage(self, username)

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.frame = master.current_frame

        tk.Label(self.frame, text="Login").pack(pady=10)
        
        tk.Label(self.frame, text="Username:").pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        tk.Label(self.frame, text="Password:").pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        tk.Button(self.frame, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.frame, text="Sign Up", command=self.master.show_signup_page).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        cursor = self.master.db_conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.master.show_welcome_page(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

class SignupPage:
    def __init__(self, master):
        self.master = master
        self.frame = master.current_frame

        tk.Label(self.frame, text="Sign Up").pack(pady=10)
        
        tk.Label(self.frame, text="Username:").pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        tk.Label(self.frame, text="Password:").pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        tk.Button(self.frame, text="Sign Up", command=self.signup).pack(pady=10)
        tk.Button(self.frame, text="Back to Login", command=self.master.show_login_page).pack()

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        cursor = self.master.db_conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.master.db_conn.commit()
            messagebox.showinfo("Success", "Account created successfully!")
            self.master.show_login_page()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"An error occurred: {err}")

class WelcomePage:
    def __init__(self, master, username):
        self.master = master
        self.frame = master.current_frame

        tk.Label(self.frame, text=f"Welcome, {username}!").pack(pady=20)
        tk.Button(self.frame, text="Logout", command=self.master.show_login_page).pack()

if __name__ == "__main__":
    app = AuthApp()
    app.mainloop()