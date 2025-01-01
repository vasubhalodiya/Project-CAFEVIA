# Function to fetch order data
def fetch_order_data():
    try:
        # Connect to the database
        con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
        cursor = con.cursor()
        
        # Query the orders table
        cursor.execute("SELECT * FROM orders")
        data = cursor.fetchall()
        return data
    except Exception as e:
        print("Error fetching order data:", e)
        return []
    finally:
        if con:
            con.close()

# Function to populate Treeview
def populate_treeview(tree):
    # Clear existing data
    for row in tree.get_children():
        tree.delete(row)
    
    # Fetch data from the database
    orders = fetch_order_data()
    
    # Insert data into the Treeview
    for order in orders:
        tree.insert("", "end", values=order)

# Create a frame for the Treeview (occupying half the page)
treeview_frame = Frame(OrderFrame, background="#f0f0f0")  # Adjust background if needed
treeview_frame.place(relx=0.03, rely=0.09, relwidth=0.95, relheight=0.5)  # Adjust relheight to 0.5 for half-page

# Define columns for the Treeview
columns = ("Order ID", "Order Name", "Customer Name", "Quantity", "Price", 
        "Total", "Discount", "Final Total", "Order Date")

# Style configuration for Treeview
style = ttk.Style()
style.configure("Custom.Treeview", background="#e6f2ff", fieldbackground="#e6f2ff", foreground="black", rowheight=25)
style.configure("Custom.Treeview.Heading", background="#004080", foreground="white", font=("Arial", 10, "bold"))

# Create the Treeview widget with custom style
tree = ttk.Treeview(treeview_frame, columns=columns, show="headings", height=10, style="Custom.Treeview")

# Configure Treeview columns
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130, anchor="center")  # Adjust column width as needed

# Add a vertical scrollbar
scrollbar = ttk.Scrollbar(treeview_frame, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)

# Pack the Treeview widget
tree.pack(fill=BOTH, expand=True)

# Populate the Treeview with data
populate_treeview(tree)