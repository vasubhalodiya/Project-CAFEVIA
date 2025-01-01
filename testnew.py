import mysql.connector
from tkinter import *
from tkinter import ttk

# MySQL connection function
def db_connect():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="your_database"
    )

# Function to insert selected data into MySQL database
def insert_data(selected_value):
    db = db_connect()
    cursor = db.cursor()

    # Assuming you have a table 'dropdown_data' with a column 'value' to store the selected value
    query = "INSERT INTO dropdown_data (value) VALUES (%s)"
    cursor.execute(query, (selected_value,))
    db.commit()  # Commit the changes
    cursor.close()
    db.close()
    print(f"Data '{selected_value}' inserted into the database!")

# Tkinter GUI class
class DropdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dropdown Example")

        # Sample data for the dropdown
        dropdown_values = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

        # Create a Combobox (dropdown) with the sample values
        self.dropdown = ttk.Combobox(self.root, values=dropdown_values)
        self.dropdown.set(dropdown_values[0])  # Set default value to the first item in the list
        self.dropdown.pack(pady=20)

        # Submit button to insert the selected value into MySQL
        submit_button = Button(self.root, text="Submit", command=self.submit)
        submit_button.pack(pady=10)

    def submit(self):
        selected_value = self.dropdown.get()  # Get the selected value from the dropdown
        insert_data(selected_value)  # Insert the selected value into the database

# Initialize Tkinter window
root = Tk()
app = DropdownApp(root)
root.mainloop()
