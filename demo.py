import tkinter as tk
from tkinter import ttk

class CustomProgressBar:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Progress Bar")
        self.root.geometry("400x200")
        
        # Configure style for the progress bar
        self.style = ttk.Style()
        self.style.configure("TProgressbar",
                             thickness=40,  # Adjust thickness
                             barcolor='blue',  # Color of progress bar
                             background='gray')  # Color of background
        
        # Create a progress bar with a custom style
        self.progress = ttk.Progressbar(self.root, length=300, style="TProgressbar")
        self.progress.place(relx=0.5, rely=0.5, anchor="center")
        
        # Start the progress
        self.start_button = tk.Button(self.root, text="Start Progress", command=self.start_progress)
        self.start_button.pack(pady=20)

    def start_progress(self):
        """Simulate a task by updating the progress bar"""
        self.progress["value"] = 0
        self.progress["maximum"] = 100
        self.update_progress(0)
        
    def update_progress(self, i):
        """Update the progress bar"""
        if i <= 100:
            self.progress["value"] = i
            self.root.after(30, self.update_progress, i + 1)  # Increment the progress after 30ms
        else:
            self.redirect_to_new_page()  # Redirect after progress reaches 100

    def redirect_to_new_page(self):
        """Redirect to a new page"""
        self.progress.place_forget()  # Remove progress bar
        self.start_button.place_forget()  # Remove start button
        new_label = tk.Label(self.root, text="You have reached the new page!", font=("Helvetica", 16))
        new_label.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomProgressBar(root)
    root.mainloop()
