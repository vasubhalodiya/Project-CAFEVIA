from tkinter import *

def create_transparent_window():
    root = Tk()
    root.geometry("400x400+100+100")  # Set the size and position of the window

    # Remove the title bar
    root.overrideredirect(True)

    # Set the background color and opacity
    root.configure(bg="black")
    root.attributes("-alpha", 0.5)  # Set opacity (0.0 to 1.0)

    # Add a close button
    close_button = Button(root, text="Close", command=root.destroy, bg="red", fg="white", borderwidth=0)
    close_button.pack(pady=20)

    # Dragging functionality
    def start_move(event):
        root.x = event.x
        root.y = event.y

    def move_window(event):
        x = root.winfo_x() + (event.x - root.x)
        y = root.winfo_y() + (event.y - root.y)
        root.geometry(f"+{x}+{y}")

    root.bind("<Button-1>", start_move)
    root.bind("<B1-Motion>", move_window)

    root.mainloop()

create_transparent_window()
