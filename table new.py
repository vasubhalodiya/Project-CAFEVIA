# Database connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="restaurant_management"  # Updated database name
)

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

def on_table_click(table_number):
    current_status = get_table_status(table_number)
    new_status = "reserved" if current_status == "available" else "available"
    update_table_status(table_number, new_status)
    messagebox.showinfo("Table Status Changed", f"Table {table_number} is now {new_status.capitalize()}!")
    refresh_tables()

def draw_table_with_chairs(canvas, relx, rely, table_width, table_height, chair_config, table_number):
    
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    x = relx * canvas_width
    y = rely * canvas_height

    # Fetch table status for coloring
    status = get_table_status(table_number)
    button_color = "green" if status == "available" else "red"

    # Table button
    table_button = Button(
        canvas,
        text=f"Table {table_number}",
        bg=button_color,
        fg="white",
        command=lambda: on_table_click(table_number)
    )
    table_button.place(x=x, y=y, width=table_width, height=table_height)

    # Chair size and spacing
    chair_size = 20
    chair_spacing = 10

    # Draw chairs (similar to original)
    for i in range(chair_config["top"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["top"]) - (chair_size / 2)
        chair_y = y - chair_size - chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="gray")

    for i in range(chair_config["bottom"]):
        chair_x = x + (i + 0.5) * (table_width / chair_config["bottom"]) - (chair_size / 2)
        chair_y = y + table_height + chair_spacing
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="gray")

    for i in range(chair_config["left"]):
        chair_x = x - chair_size - chair_spacing
        chair_y = y + (i + 0.5) * (table_height / chair_config["left"]) - (chair_size / 2)
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="gray")

    for i in range(chair_config["right"]):
        chair_x = x + table_width + chair_spacing
        chair_y = y + (i + 0.5) * (table_height / chair_config["right"]) - (chair_size / 2)
        canvas.create_rectangle(chair_x, chair_y, chair_x + chair_size, chair_y + chair_size, fill="gray")

def refresh_tables():
    canvas.delete("all")
    draw_tables()

def draw_tables():
    draw_table_with_chairs(canvas, 0.1, 0.1, 100, 70, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 1)
    draw_table_with_chairs(canvas, 0.3, 0.1, 100, 70, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 2)
    draw_table_with_chairs(canvas, 0.5, 0.1, 100, 70, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 3)
    draw_table_with_chairs(canvas, 0.7, 0.1, 100, 70, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 4)
    draw_table_with_chairs(canvas, 0.9, 0.1, 100, 70, {"top": 2, "bottom": 2, "left": 1, "right": 1}, 5)

canvas = Canvas(TableBookFrame, bg="white", bd=0, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Draw tables
draw_tables()
