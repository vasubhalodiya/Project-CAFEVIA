import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

parent_frame = tk.Frame(root)
parent_frame.pack(fill="both", expand=True)

row = 0
col = 0

def add_dynamic_frame():
    global row, col
    new_frame = tk.Frame(parent_frame, width=100, height=100, bg="lightblue", relief="solid", bd=2)
    new_frame.grid(row=row, column=col, padx=5, pady=5)

    label = tk.Label(new_frame, text=f"Child Frame {row*4 + col + 1}")
    label.pack(padx=10, pady=10)

    col += 1
    if col > 2:
        col = 0
        row += 1

for _ in range(5):
    add_dynamic_frame()

root.mainloop()
