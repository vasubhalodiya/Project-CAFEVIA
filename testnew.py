import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Replace with your MySQL username
        password="",         # Replace with your MySQL password
        database="table_booking_system"
    )

# Fetch all tables from the database
def fetch_tables():
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tables")
        tables = cursor.fetchall()
        db.close()
        return tables
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return []

# Update the table status in the database
def update_table_status(table_id, new_status):
    try:
        db = connect_db()
        cursor = db.cursor()
        query = "UPDATE tables SET status = %s WHERE id = %s"
        cursor.execute(query, (new_status, table_id))
        db.commit()
        db.close()
        messagebox.showinfo("Success", f"Table {table_id} is now {new_status}.")
        refresh_ui()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Refresh the UI to reflect updated table statuses
def refresh_ui():
    for widget in root.winfo_children():
        widget.destroy()
    render_ui()

# Render the UI with table statuses
def render_ui():
    tables = fetch_tables()

    if not tables:
        tk.Label(root, text="No tables available.", font=("Arial", 12)).pack()
        return

    tk.Label(root, text="Table Booking System", font=("Arial", 16)).pack(pady=10)

    for table in tables:
        table_id, table_number, status = table
        color = "green" if status == "available" else "red"
        button_text = f"Table {table_number}\n({status.capitalize()})"

        btn = tk.Button(root, text=button_text, bg=color, fg="white", width=15, height=3, command=lambda tid=table_id, stat=status: toggle_table_status(tid, stat))
        btn.pack(pady=5)

# Toggle table status between 'available' and 'reserved'
def toggle_table_status(table_id, current_status):
    new_status = "available" if current_status == "reserved" else "reserved"
    update_table_status(table_id, new_status)

# Automatically reset all tables to 'available' after 2 hours (7200000 milliseconds)
def auto_reset_tables():
    try:
        db = connect_db()
        cursor = db.cursor()
        query = "UPDATE tables SET status = 'available'"
        cursor.execute(query)
        db.commit()
        db.close()
        messagebox.showinfo("Reset", "All tables are now available.")
        refresh_ui()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

    # Schedule the reset again after 2 hours (7200000 milliseconds)
    root.after(10000, auto_reset_tables)  # 2 hours = 2 * 60 * 60 * 1000 ms

# Main window setup
root = tk.Tk()
root.title("Table Booking System")
root.geometry("400x400")

# Call the auto_reset_tables function to start the automatic reset process
auto_reset_tables()

# Initial UI rendering
render_ui()

root.mainloop()
