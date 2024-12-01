import tkinter as tk
from tkinter import messagebox, Toplevel, StringVar

class TableBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Table Booking System")
        
        self.orders = []  # Store order details
        self.num_tables = 10
        self.table_status = ["Available"] * self.num_tables
        
        self.table_buttons = []
        for i in range(self.num_tables):
            button = tk.Button(
                root,
                text=f"Table {i + 1}",
                width=12,
                height=2,
                bg="lightgreen",
                command=lambda i=i: self.handle_table(i)
            )
            button.grid(row=i // 5, column=i % 5, padx=10, pady=10)
            self.table_buttons.append(button)
        
        # Button to show order details
        order_btn = tk.Button(root, text="View Order Details", command=self.view_order_details)
        order_btn.grid(row=2, column=0, columnspan=5, pady=20)

    def handle_table(self, table_index):
        """Handle table booking or unbooking."""
        if self.table_status[table_index] == "Available":
            self.open_booking_form(table_index)
        else:
            self.open_payment_form(table_index)

    def open_booking_form(self, table_index):
        """Open a form to book a table."""
        form = Toplevel(self.root)
        form.title("Booking Form")

        tk.Label(form, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        name_var = StringVar()
        tk.Entry(form, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form, text="Contact No:").grid(row=1, column=0, padx=10, pady=5)
        contact_var = StringVar()
        tk.Entry(form, textvariable=contact_var).grid(row=1, column=1, padx=10, pady=5)

        def submit_booking():
            name = name_var.get()
            contact = contact_var.get()
            if not name or not contact:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            self.table_status[table_index] = "Booked"
            self.table_buttons[table_index].config(bg="red", text=f"Table {table_index + 1}\nBooked")
            self.orders.append({
                "table": table_index + 1,
                "name": name,
                "contact": contact,
                "payment": None
            })
            messagebox.showinfo("Success", f"Table {table_index + 1} booked successfully!")
            form.destroy()

        tk.Button(form, text="Submit", command=submit_booking).grid(row=2, column=0, columnspan=2, pady=10)

    def open_payment_form(self, table_index):
        """Open a form to make payment and unbook the table."""
        form = Toplevel(self.root)
        form.title("Payment Form")

        tk.Label(form, text="Enter Amount (₹):").grid(row=0, column=0, padx=10, pady=5)
        amount_var = StringVar()
        tk.Entry(form, textvariable=amount_var).grid(row=0, column=1, padx=10, pady=5)

        def submit_payment():
            amount = amount_var.get()
            if not amount.isdigit():
                messagebox.showerror("Error", "Please enter a valid amount.")
                return

            # Update order with payment
            for order in self.orders:
                if order["table"] == table_index + 1 and order["payment"] is None:
                    order["payment"] = int(amount)
                    break

            self.table_status[table_index] = "Available"
            self.table_buttons[table_index].config(bg="lightgreen", text=f"Table {table_index + 1}")
            messagebox.showinfo("Success", f"Payment received for Table {table_index + 1}.")
            form.destroy()

        tk.Button(form, text="Submit", command=submit_payment).grid(row=1, column=0, columnspan=2, pady=10)

    def view_order_details(self):
        """Display the order details."""
        details = Toplevel(self.root)
        details.title("Order Details")

        tk.Label(details, text="Table", width=10).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(details, text="Name", width=20).grid(row=0, column=1, padx=10, pady=5)
        tk.Label(details, text="Contact", width=20).grid(row=0, column=2, padx=10, pady=5)
        tk.Label(details, text="Payment (₹)", width=15).grid(row=0, column=3, padx=10, pady=5)

        for i, order in enumerate(self.orders):
            tk.Label(details, text=order["table"], width=10).grid(row=i + 1, column=0, padx=10, pady=5)
            tk.Label(details, text=order["name"], width=20).grid(row=i + 1, column=1, padx=10, pady=5)
            tk.Label(details, text=order["contact"], width=20).grid(row=i + 1, column=2, padx=10, pady=5)
            tk.Label(details, text=order["payment"] if order["payment"] else "-", width=15).grid(row=i + 1, column=3, padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = TableBookingApp(root)
    root.mainloop()
