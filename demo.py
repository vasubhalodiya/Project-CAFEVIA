import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a label with specific width and wraplength
label = tk.Label(root, 
                 text="This is a long text that will automatically wrap when the width exceeds the set limit.", 
                 width=100, 
                 wraplength=150,  # Specify the maximum width for wrapping text
                 anchor="w",  # Align text to the left
                 font=("Helvetica", 12))
label.pack(padx=10, pady=20)

root.mainloop()
