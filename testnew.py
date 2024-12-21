from tkinter import Tk, Canvas, Button, messagebox

primary_color = "brown"
secondary_color = "white"
price_color = "blue"

def on_table_click(table_number):
    """
    Handle table button click.
    :param table_number: The number of the table clicked.
    """
    messagebox.showinfo("Table Clicked", f"You clicked Table {table_number}!")

def draw_table_with_chairs(canvas, relx, rely, table_width, table_height, chair_config, table_number):
    """
    Draws a table as a button with simple chairs around it on a canvas.
    The table and chair positions are determined using relative coordinates (relx, rely).
    
    :param canvas: The Canvas widget.
    :param relx: Relative x-position of the table (0.0 to 1.0).
    :param rely: Relative y-position of the table (0.0 to 1.0).
    :param table_width: Width of the table.
    :param table_height: Height of the table.
    :param chair_config: A dictionary specifying the number of chairs on each side:
                         {"top": int, "bottom": int, "left": int, "right": int}.
    :param table_number: The number assigned to the table.
    """
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    # Calculate the absolute position based on relative position
    x = relx * canvas_width
    y = rely * canvas_height
    
    # Chair size and spacing
    chair_size = 20
    chair_spacing = 10

    # Table button
    table_button = Button(canvas, text=f"Table {table_number}", bg=primary_color, fg=secondary_color, command=lambda: on_table_click(table_number))
    table_button.place(x=x, y=y, width=table_width, height=table_height)

    # Draw chairs on the top side
    for i in range(chair_config["top"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["top"]) - (chair_size / 2)
        chair_y = y - chair_size - chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=price_color)

    # Draw chairs on the bottom side
    for i in range(chair_config["bottom"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["bottom"]) - (chair_size / 2)
        chair_y = y + table_height + chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=price_color)

    # Draw chairs on the left side
    for i in range(chair_config["left"]):
        chair_x = x - chair_size - chair_spacing
        chair_y = y + (i + 0.5) * (table_height / chair_config["left"]) - (chair_size / 2)
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=price_color)

    # Draw chairs on the right side
    for i in range(chair_config["right"]):
        chair_x = x + table_width + chair_spacing
        chair_y = y + (i + 0.5) * (table_height / chair_config["right"]) - (chair_size / 2)
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill=price_color)

# Main application window
root = Tk()
root.title("Table with Chairs")
root.geometry("1000x700")

# Create Canvas
canvas = Canvas(root, bg=secondary_color, bd=0, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Draw tables with different configurations using relative positioning
draw_table_with_chairs(canvas, 0.05, 0.05, 110, 70, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 1)  # Table 1
draw_table_with_chairs(canvas, 0.27, 0.05, 150, 70, {"top": 3, "bottom": 3, "left": 2, "right": 2}, 2)  # Table 2
draw_table_with_chairs(canvas, 0.54, 0.05, 110, 70, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 3)  # Table 3
draw_table_with_chairs(canvas, 0.77, 0.05, 180, 70, {"top": 4, "bottom": 4, "left": 2, "right": 2}, 4)  # Table 4

root.mainloop()
