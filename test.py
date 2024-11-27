import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Right Side Border")

# Create a main frame
main_frame = tk.Frame(root, width=300, height=200, bg="white")
main_frame.pack_propagate(False)
main_frame.pack(padx=10, pady=10)

# Add a border on the right side
right_border = tk.Frame(main_frame, bg="black", width=2)
right_border.pack(side="right", fill="y")

# Add content in the main frame
content = tk.Label(main_frame, text="Frame with Right Border", bg="white")
content.pack(pady=20, padx=20)

# Run the application
root.mainloop()
