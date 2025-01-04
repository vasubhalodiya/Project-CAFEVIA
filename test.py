import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your host
            user="root",       # Replace with your MySQL username
            password="",       # Replace with your MySQL password
            database="logininfo"  # Replace with your database name
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return

    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM userlogin WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        connection.close()

        if result:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            open_new_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

# Function to open another window and close the login window
def open_new_window():
    root.destroy()  # Close the login window

    new_window = tk.Tk()  # Create the main dashboard window
    new_window.title("Dashboard")
    new_window.geometry("300x200")
    tk.Label(new_window, text="Welcome to the Dashboard!", font=("Arial", 14)).pack(pady=50)
    new_window.mainloop()

# Main Tkinter window
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

# UI components
tk.Label(root, text="Username:", font=("Arial", 12)).pack(pady=5)
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

tk.Label(root, text="Password:", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Login", font=("Arial", 12), command=login)
login_button.pack(pady=20)

root.mainloop()
