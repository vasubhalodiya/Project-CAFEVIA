from tkinter import *
import tkinter as tk
import tkinter
from tkinter import ttk
import os
from tkinter import messagebox
from tkinter import PhotoImage

root = Tk()
root.state('zoomed')
root.resizable(False, False)
root.title("Listenary")
root.wm_iconbitmap('images\logo.ico')
root.configure(bg="#fff")

# =============================================================================

def dashboard():
    dashboard_fram = Frame(width=800, height=600, bg='yellow')
    dashboard_fram.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

def playlist():
    playlist_fram = Frame(width=800, height=600, bg='green')
    playlist_fram.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

def artist():
    artist_fram = Frame(width=800, height=600, bg='red')
    artist_fram.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

def user():
    user_fram = Frame(width=800, height=600, bg='blue')
    user_fram.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

def category():
    category_fram = Frame(width=800, height=600, bg='pink')
    category_fram.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

def logout():
    logout_fram = Frame(width=800, height=600, bg='pink')
    logout_fram.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

def profile():
    profile_fram = Frame(width=800, height=600, bg='pink')
    profile_fram.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

def click(*args): 
    search_box.delete(0, 'end') 
  
def leave(*args): 
    search_box.delete(0, 'end') 
    search_box.insert(0, 'Search here') 
    root.focus() 
# ======================MenuBar=======================================================

menu_bar = Frame(bg="#111013",height=100)
menu_bar.place(relx=0, rely=0, relwidth=0.18, relheight=1)

right_border = Frame(menu_bar, bg="#818594", width=1)
right_border.pack(side="right", fill="y")

# logo
menu_logo = Label(menu_bar, text="LISTENARY", bg="#232323", fg="#000")
menu_logo.place(relx=0.2, rely=0.05)
menu_logo.config(bg="#111013", fg="#fff", font=("Arsenal", 20, "bold"))

# dashboard button
menu_dashboard = Button(menu_bar, text='Dashboard', bg='#fff', fg='#000', command=dashboard, font=("Arsenal", 11), bd=0, cursor="hand2")
menu_dashboard.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.05)

# playlist button
menu_playlist = Button(menu_bar, text='Playlist', bg='#fff', fg='#000', command=playlist, font=("Arsenal", 11), bd=0, cursor="hand2")
menu_playlist.place(relx=0.1, rely=0.31, relwidth=0.8, relheight=0.05)

# artist button
menu_artist = Button(menu_bar, text='Artist', bg='#fff', fg='#000', command=artist, font=("Arsenal", 11), bd=0, cursor="hand2")
menu_artist.place(relx=0.1, rely=0.23, relwidth=0.8, relheight=0.05)

# user button
menu_user = Button(menu_bar, text='User', bg='#fff', fg='#000', command=user, font=("Arsenal", 11), bd=0, cursor="hand2")
menu_user.place(relx=0.1, rely=0.39, relwidth=0.8, relheight=0.05)

# category button
menu_category = Button(menu_bar, text='Category', bg='#fff', fg='#000', command=category, font=("Arsenal", 11), bd=0, cursor="hand2")
menu_category.place(relx=0.1, rely=0.47, relwidth=0.8, relheight=0.05)

# logout button
menu_logout = Button(menu_bar, text='Logout', bg='#fff', fg='#000', command=logout, font=("Arsenal", 11), bd=0, cursor="hand2")
menu_logout.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.05)

# =====================ProfileNavbar========================================================

navbar = Frame(bg="#111013")
navbar.place(relx=0.18, rely=0, relwidth=0.82, relheight=0.06)

# profile button
profile_btn = Button(navbar, text='V', bg='#fff', fg='#000', command=logout, font=("Arsenal", 11, "bold"), bd=0, cursor="hand2")
profile_btn.place(relx=0.97, rely=0.25, relwidth=0.02, relheight=0.5)

# profile-name button
profile_name_btn = Label(navbar, text='Vasu', bg='#111013', fg='#fff', font=("Arsenal", 10, "bold"), bd=0, cursor="hand2")
profile_name_btn.place(relx=0.93, rely=0.25, relwidth=0.04, relheight=0.5)

# # =====================ContentSection========================================================

# cnt_sec = Frame(bg="#fff")
# cnt_sec.place(relx=0.18, rely=0, relwidth=0.82, relheight=1)

search_box = Entry(navbar)
search_box.place(relx=0.02, rely=0.25, relwidth=0.2, relheight=0.5)
search_box.insert(0, 'Search here') 
search_box.bind("<Button-1>", click) 
search_box.bind("<Leave>", leave) 
















































root.mainloop()