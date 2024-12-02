from tkinter import Tk, Frame

# Create the main window
root = Tk()
root.geometry("400x300")  # Set window size
root.configure(bg="white")

# Create a main Frame
main_frame = Frame(root, bg="lightgray")
main_frame.place(relwidth=1, relheight=1)

# Create a top border by adding a thin Frame
top_border = Frame(main_frame, bg="black", height=2)  # Adjust `height` for border thickness
top_border.pack(side="top", fill="x")  # Attach it to the top and stretch across the width

root.mainloop()
