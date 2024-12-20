import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="login_system"
    )

# Redirect to another page
def redirect_to_dashboard():
    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("300x200")

    tk.Label(dashboard, text="Welcome to the Dashboard!", font=("Arial", 16)).pack(pady=20)
    tk.Button(dashboard, text="Logout", command=lambda: dashboard.destroy()).pack(pady=10)

# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    try:
        db = connect_db()
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            root.withdraw()  # Hide the login window
            redirect_to_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password.")
        
        db.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# GUI setup
root = tk.Tk()
root.title("Login System")
root.geometry("300x150")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
