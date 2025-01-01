import MySQLdb
from tkinter import *
from tkinter import ttk

# Function to fetch order data
def fetch_order_data():
    try:
        # Connect to the database
        con = MySQLdb.connect(host="localhost", user="OrderFrame", password="", database="cafevia")
        cursor = con.cursor()
        
        # Query the orders table
        cursor.execute("SELECT orderid, ordername, customername, orderqty, orderprice, ordertotal, orderdiscount, order_final_total, orderdate FROM orders")
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

# Main application window
OrderFrame = Tk()
OrderFrame.title("Order Data")
OrderFrame.geometry("1200x500")  # Adjust window size for all columns

# Define columns for the Treeview
columns = ("Order ID", "Order Name", "Customer Name", "Quantity", "Price", 
           "Total", "Discount", "Final Total", "Order Date")

# Create the Treeview widget
tree = ttk.Treeview(OrderFrame, columns=columns, show="headings", height=20)

# Configure Treeview columns
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")  # Adjust column width as needed

# Add a vertical scrollbar
scrollbar = ttk.Scrollbar(OrderFrame, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)

# Pack the Treeview widget
tree.pack(fill=BOTH, expand=True)

# Populate the Treeview with data
populate_treeview(tree)

# Run the application
OrderFrame.mainloop()
