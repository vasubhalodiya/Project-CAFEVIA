import tkinter as tk

def open_subwindow():
    # Create a subwindow (Toplevel)
    top = tk.Toplevel(root)
    top.title("Subwindow")
    
    # Make sure the subwindow stays on top of the main window
    top.attributes("-topmost", 1)
    top.lift()

    # Function to show a custom message box
    def show_message():
        # Create a custom message box (another Toplevel window)
        message_box = tk.Toplevel(top)
        message_box.title("Custom Message Box")
        
        # Make the message box stay on top of the subwindow
        message_box.attributes("-topmost", 1)
        message_box.lift()

        label = tk.Label(message_box, text="This is a custom message.")
        label.pack(pady=20)

        button = tk.Button(message_box, text="OK", command=message_box.destroy)
        button.pack(pady=10)

    # Create a button in the subwindow that shows the custom message box
    button = tk.Button(top, text="Show Message", command=show_message)
    button.pack(pady=20)

root = tk.Tk()
root.title("Main Window")

main_button = tk.Button(root, text="Open Subwindow", command=open_subwindow)
main_button.pack(pady=20)

root.mainloop()
