import tkinter as tk
from tkinter import messagebox

def on_table_click(table_number):
    """
    Handle table button click.
    :param table_number: The number of the table clicked.
    """
    messagebox.showinfo("Table Clicked", f"You clicked Table {table_number}!")

def draw_table_with_rounded_border(canvas, x, y, table_width, table_height, chair_config, table_number):
    """
    Draws a table as a button with rounded borders and chairs around it on a canvas.

    :param canvas: The Canvas widget.
    :param x: Top-left x-coordinate of the table.
    :param y: Top-left y-coordinate of the table.
    :param table_width: Width of the table.
    :param table_height: Height of the table.
    :param chair_config: A dictionary specifying the number of chairs on each side:
                         {"top": int, "bottom": int, "left": int, "right": int}.
    :param table_number: The number assigned to the table.
    """
    # Chair size and spacing
    chair_size = 20
    chair_spacing = 10
    radius = 15  # Radius for rounded corners

    # Draw the table as a rounded rectangle
    canvas.create_oval(x, y, x + radius*2, y + radius*2, fill="brown", outline="black")  # Top-left corner
    canvas.create_oval(x + table_width - radius*2, y, x + table_width, y + radius*2, fill="brown", outline="black")  # Top-right corner
    canvas.create_oval(x, y + table_height - radius*2, x + radius*2, y + table_height, fill="brown", outline="black")  # Bottom-left corner
    canvas.create_oval(x + table_width - radius*2, y + table_height - radius*2, x + table_width, y + table_height, fill="brown", outline="black")  # Bottom-right corner
    
    # Draw the edges of the table (without corners)
    canvas.create_rectangle(x + radius, y, x + table_width - radius, y + table_height, fill="brown", outline="black")  # Top and bottom edges
    canvas.create_rectangle(x, y + radius, x + table_width, y + table_height - radius, fill="brown", outline="black")  # Left and right edges

    # Table button
    table_button = tk.Button(canvas, text=f"Table {table_number}", bg="brown", fg="white", command=lambda: on_table_click(table_number))
    table_button.place(x=x + radius, y=y + radius, width=table_width - radius*2, height=table_height - radius*2)

    # Draw chairs on the top side
    for i in range(chair_config["top"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["top"]) - (chair_size / 2)
        chair_y = y - chair_size - chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="blue")

    # Draw chairs on the bottom side
    for i in range(chair_config["bottom"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["bottom"]) - (chair_size / 2)
        chair_y = y + table_height + chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="blue")

    # Draw chairs on the left side
    for i in range(chair_config["left"]):
        chair_x = x - chair_size - chair_spacing
        chair_y = y + (i + 0.5) * (table_height / chair_config["left"]) - (chair_size / 2)
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="blue")

    # Draw chairs on the right side
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

# Draw tables with different configurations
draw_table_with_rounded_border(canvas, 50, 50, 100, 50, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 1)  # Table 1
draw_table_with_rounded_border(canvas, 200, 100, 150, 70, {"top": 3, "bottom": 3, "left": 2, "right": 2}, 2)  # Table 2
draw_table_with_rounded_border(canvas, 400, 200, 120, 60, {"top": 2, "bottom": 2, "left": 3, "right": 3}, 3)  # Table 3
draw_table_with_rounded_border(canvas, 600, 300, 140, 80, {"top": 4, "bottom": 4, "left": 2, "right": 2}, 4)  # Table 4

root.mainloop()
