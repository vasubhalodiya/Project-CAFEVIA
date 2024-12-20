import tkinter as tk
from tkinter import messagebox

def on_table_click(table_number):
    messagebox.showinfo("Table Clicked", f"You clicked Table {table_number}!")

def draw_table_with_chairs(canvas, x, y, table_width, table_height, chair_config, table_number):
    
    # Chair size and spacing
    chair_size = 20
    chair_spacing = 10

    # Table button
    table_button = tk.Button(canvas, text=f"Table {table_number}", bg="brown", fg="white", command=lambda: on_table_click(table_number))
    table_button.place(x=x, y=y, width=table_width, height=table_height)

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
draw_table_with_chairs(canvas, 50, 50, 100, 50, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 1)  # Table 1
draw_table_with_chairs(canvas, 200, 100, 150, 70, {"top": 3, "bottom": 3, "left": 2, "right": 2}, 2)  # Table 2
draw_table_with_chairs(canvas, 400, 200, 120, 60, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 3)  # Table 3
draw_table_with_chairs(canvas, 600, 300, 140, 80, {"top": 4, "bottom": 4, "left": 2, "right": 2}, 4)  # Table 4

root.mainloop()
