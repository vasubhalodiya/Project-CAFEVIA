import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL connection setup
def get_table_status(table_id):
    """
    Fetches the current status of the table from the database.
    :param table_id: The ID of the table.
    :return: The status of the table ('available' or 'reserved').
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="restaurant"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT status FROM tables WHERE id = {table_id}")
        result = cursor.fetchone()
        return result[0] if result else "available"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "available"
    finally:
        if connection:
            connection.close()

def update_table_status(table_id, status):
    """
    Updates the table status in the database.
    :param table_id: The ID of the table.
    :param status: The new status to be set ('available' or 'reserved').
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="restaurant"
        )
        cursor = connection.cursor()
        cursor.execute(f"UPDATE tables SET status = %s WHERE id = %s", (status, table_id))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection:
            connection.close()

def on_table_click(table_id):
    """
    Handle table button click and update the table status.
    :param table_id: The ID of the table clicked.
    """
    current_status = get_table_status(table_id)
    new_status = "reserved" if current_status == "available" else "available"
    update_table_status(table_id, new_status)
    
    # Update button color based on the new status
    update_table_button_color(table_id)

def update_table_button_color(table_id):
    """
    Update the table button color based on the status.
    :param table_id: The ID of the table.
    """
    status = get_table_status(table_id)
    color = "green" if status == "available" else "red"
    
    table_buttons[table_id].config(bg=color)

def draw_table_with_chairs(canvas, x, y, table_width, table_height, chair_config, table_id):
    """
    Draws a table as a button with chairs around it on a canvas.
    :param canvas: The Canvas widget.
    :param x: Top-left x-coordinate of the table.
    :param y: Top-left y-coordinate of the table.
    :param table_width: Width of the table.
    :param table_height: Height of the table.
    :param chair_config: A dictionary specifying the number of chairs on each side.
    :param table_id: The ID assigned to the table.
    """
    global table_buttons
    # Chair size and spacing
    chair_size = 20
    chair_spacing = 10

    # Get initial table status
    status = get_table_status(table_id)
    color = "green" if status == "available" else "red"

    # Table button
    table_button = tk.Button(canvas, text=f"Table {table_id}", bg=color, fg="white", command=lambda: on_table_click(table_id))
    table_button.place(x=x, y=y, width=table_width, height=table_height)

    # Store table button for later updates
    table_buttons[table_id] = table_button

    # Draw chairs around the table (same as before)
    # Top chairs
    for i in range(chair_config["top"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["top"]) - (chair_size / 2)
        chair_y = y - chair_size - chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="blue")

    # Bottom chairs
    for i in range(chair_config["bottom"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["bottom"]) - (chair_size / 2)
        chair_y = y + table_height + chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="blue")

    # Left chairs
    for i in range(chair_config["left"]):
        chair_x = x - chair_size - chair_spacing
        chair_y = y + (i + 0.5) * (table_height / chair_config["left"]) - (chair_size / 2)
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="blue")

    # Right chairs
    for i in range(chair_config["right"]):
        chair_x = x + table_width + chair_spacing
        chair_y = y + (i + 0.5) * (table_height / chair_config["right"]) - (chair_size / 2)
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="blue")


# Main application window
root = tk.Tk()
root.title("Table with Chairs")
root.geometry("800x600")

# Create Canvas
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack(fill="both", expand=True)

# Initialize a dictionary to store buttons
table_buttons = {}

# Draw tables with different configurations
draw_table_with_chairs(canvas, 50, 50, 100, 50, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 1)  # Table 1
draw_table_with_chairs(canvas, 200, 100, 150, 70, {"top": 3, "bottom": 3, "left": 2, "right": 2}, 2)  # Table 2
draw_table_with_chairs(canvas, 400, 200, 120, 60, {"top": 2, "bottom": 2, "left": 3, "right": 3}, 3)  # Table 3
draw_table_with_chairs(canvas, 600, 300, 140, 80, {"top": 4, "bottom": 4, "left": 2, "right": 2}, 4)  # Table 4

root.mainloop()
