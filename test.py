import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Sample MySQL connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="restaurant_management"  # Replace with your database name
    )

# Initialize root window
root = tk.Tk()
root.title("Table Booking System")
root.geometry("1200x800")

# Global color settings
primary_color = "#4CAF50"  # Green color for available tables
secondary_color = "#FFFFFF"  # White color for text
price_color = "#FF9800"  # Price color for available chairs

# Table buttons dictionary to store references
table_buttons = {}

# Database connection setup
db = connect_db()
cursor = db.cursor()

# Fetch table status from the database
def get_table_status(table_number):
    cursor.execute("SELECT status FROM table_reservations WHERE table_number = %s", (table_number,))
    result = cursor.fetchone()
    return result[0] if result else "available"

# Update table status in the database
def update_table_status(table_number, status):
    cursor.execute("UPDATE table_reservations SET status = %s WHERE table_number = %s", (status, table_number))
    db.commit()

# Handle table click to update status and color
def on_table_click(table_number):
    current_status = get_table_status(table_number)
    new_status = "reserved" if current_status == "available" else "available"
    update_table_status(table_number, new_status)

    # Fetch the updated status
    status = get_table_status(table_number)
    button_color = primary_color if status == "available" else "#F02533"  # Red color

    # Update the button color directly
    table_buttons[table_number].config(bg=button_color)

    # Show the messagebox
    messagebox.showinfo("Table Status Changed", f"Table {table_number} is now {new_status.capitalize()}!")

# Draw table with chairs and status button
def draw_table_with_chairs(canvas, relx, rely, table_width, table_height, chair_config, table_number):
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Calculate the absolute position based on relative position
    x = relx * canvas_width
    y = rely * canvas_height

    # Fetch table status for coloring
    status = get_table_status(table_number)
    button_color = primary_color if status == "available" else "#F02533"  # Red color
    chair_color = price_color if status == "available" else "#CECECE"  # Grey color

    # Table button
    table_buttons[table_number] = tk.Button(
        canvas,
        text=f"Table {table_number}",
        bg=button_color,
        fg=secondary_color,
        command=lambda: on_table_click(table_number),
        relief="flat"
    )
    table_buttons[table_number].place(x=x, y=y, width=table_width, height=table_height)

    # Chair size and spacing
    chair_size = 20
    chair_spacing = 10

    # Draw chairs on the top side
    for i in range(chair_config["top"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["top"]) - (chair_size / 2)
        chair_y = y - chair_size - chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=chair_color, outline="")

    # Draw chairs on the bottom side
    for i in range(chair_config["bottom"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["bottom"]) - (chair_size / 2)
        chair_y = y + table_height + chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=chair_color, outline="")

    # Draw chairs on the left side
    for i in range(chair_config["left"]):
        chair_x = x - chair_size - chair_spacing
        chair_y = y + (i + 0.5) * (table_height / chair_config["left"]) - (chair_size / 2)
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=chair_color, outline="")

    # Draw chairs on the right side
    for i in range(chair_config["right"]):
        chair_x = x + table_width + chair_spacing
        chair_y = y + (i + 0.5) * (table_height / chair_config["right"]) - (chair_size / 2)
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=chair_color, outline="")

# Create Canvas for drawing tables
canvas = tk.Canvas(root, bg=secondary_color, bd=0, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Function to draw all tables
def draw_tables():
    # Draw tables with different configurations
    draw_table_with_chairs(canvas, 0.05, 0.05, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 1)   # Table 1
    draw_table_with_chairs(canvas, 0.25, 0.05, 150, 90, {"top": 3, "bottom": 3, "left": 2, "right": 2}, 2)  # Table 2
    draw_table_with_chairs(canvas, 0.45, 0.05, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 3)  # Table 3
    draw_table_with_chairs(canvas, 0.65, 0.05, 180, 90, {"top": 4, "bottom": 4, "left": 2, "right": 2}, 4)  # Table 4
    draw_table_with_chairs(canvas, 0.85, 0.05, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 5)  # Table 5

    # Row 2
    draw_table_with_chairs(canvas, 0.05, 0.35, 150, 90, {"top": 3, "bottom": 3, "left": 1, "right": 1}, 6)   # Table 6
    draw_table_with_chairs(canvas, 0.25, 0.35, 110, 90, {"top": 2, "bottom": 2, "left": 2, "right": 2}, 7)  # Table 7
    draw_table_with_chairs(canvas, 0.45, 0.35, 110, 90, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 8)  # Table 8
    draw_table_with_chairs(canvas, 0.65, 0.35, 150, 90, {"top": 3, "bottom": 3, "left": 2, "right": 2}, 9)  # Table 9
    draw_table_with_chairs(canvas, 0.85, 0.35, 140, 90, {"top": 3, "bottom": 3, "left": 1, "right": 1}, 10)  # Table 10

# Draw tables on window load
draw_tables()

# Run the Tkinter event loop
root.mainloop()
