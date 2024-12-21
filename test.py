# Connect to MySQL database
def connect_db():
    return MySQLdb.connect(
    host="localhost",
    user="root",         # Replace with your MySQL username
    password="",         # Replace with your MySQL password
    database="bookmyshow"
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
    except MySQLdb.Error as err:
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
    except MySQLdb.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Refresh the UI to reflect updated table statuses
def refresh_ui():
    for widget in TicketBookingFrame.winfo_children():
        widget.destroy()
    render_ui()

# Render the UI with table statuses
def render_ui():
    tables = fetch_tables()

if not tables:
    Label(TicketBookingFrame, text="No tables available.", font=("Arial", 12)).pack()
    return

Label(TicketBookingFrame, text="Table Booking System", font=("Arial", 16)).pack(pady=10)

for table in tables:
    table_id, table_number, status = table
    color = "green" if status == "available" else "red"
    button_text = f"Table {table_number}\n({status.capitalize()})"

btn = Button(TicketBookingFrame, text=button_text, bg=color, fg="white", width=15, height=3, command=lambda tid=table_id, stat=status: toggle_table_status(tid, stat) )
btn.pack(pady=5)

# Toggle table status between 'available' and 'reserved'
def toggle_table_status(table_id, current_status):
    new_status = "available" if current_status == "reserved" else "reserved"
    update_table_status(table_id, new_status)

render_ui()