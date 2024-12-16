from tkinter import *
from tkinter import ttk, messagebox
import MySQLdb

root = Tk()
root.state('zoomed')

# INSERT function
def Movieinsert():
    txtttt = txt.get()

    if(txtttt==""):
        messagebox.showinfo("Insert Status","All fields are required")
    else:
        con = MySQLdb.connect(host="localhost", user="root", password="", database="try")
        cursor = con.cursor()
        cursor.execute("insert into vasu_try_table values('"+txtttt+"')")
        cursor.execute("commit")
        messagebox.showinfo("INSERT Status","INSERTED SUCCESSFULLY")
        con.close()


lbl= Label(root,text="MOVIE NAME :",font=('century gothic bold',15),background='#880808',foreground='white')
lbl.place(x=50,y=150)

txt = Entry(root,font=('century gothic',15),width=20,relief='ridge')
txt.place(x=50,y=180)

Btn = Button(root,text="ADDDDDDD",font=("century gothic bold",10),width=15,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=Movieinsert)
Btn.place(x=50,y=250)


root.mainloop()