from tkinter import *
import tkinter as tk
import tkinter
from tkinter import ttk
import os
from tkinter import messagebox

root = Tk()
root.state('zoomed')
root.resizable(False, False)
root.title("Cafevia")
root.wm_iconbitmap('images\logo.ico')
root.configure(bg="#1f1f1f")

login = Frame(bg="white",height=100)
login.place(relx=0.35, rely=0.2, relwidth=0.3)

login_head = tk.Label(login, text="CAFEVIA")
login_head.pack(padx=20, pady=20)
login_head.config(bg="#fff", font=("Arsenal", 20, "bold"))
login_head.config()













root.mainloop()