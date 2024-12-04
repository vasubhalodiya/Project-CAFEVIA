from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import MySQLdb

# LOGIN FORM CREATE
class Login:
    def _init_(self, loginwindow):
        self.loginwindow = loginwindow
        self.loginwindow.title("BOOK MY SHOW - LOGIN")
        self.loginwindow.geometry("1000x600")
        p1 = PhotoImage(file = 'images/logo1.png')
        self.loginwindow.iconphoto(False,p1)
        self.loginwindow.state('normal')
        self.main_window()
        
    def main_window(self):

        # User verifaction
        name_var=StringVar()
        passw_var=StringVar()

        # Replace with your actual image path
        bg_image = Image.open("images/login_background.jpg")
        bg_image = bg_image.resize((1000, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        # Create Canvas
        canvas = Canvas(self.loginwindow, width=1000, height=600)
        canvas.pack(fill="both", expand=True)
        # Add the image to the Canvas
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        loginframe = Frame(loginwindow,background='#880808',height=450,width=800)
        loginframe.place(x=100,y=80)

        loginframe_sub = Frame(loginwindow,background='white',height=450,width=400)
        loginframe_sub.place(x=500,y=80)

        loginframe_leftside = Frame(loginframe,background='#880808',height=400,width=360,highlightthickness=2,highlightbackground='white')
        loginframe_leftside.place(x=20,y=25)

        LoginBtn = Button(loginframe_leftside,text="LOGIN",font=('Bodoni Bd BT',10),width=27,height=2,bg='white',fg='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief='raised',activebackground='#880808',bd=3,command=win)
        LoginBtn.place(x=65,y=280)

        Loginlbl = Label(loginframe_leftside,text="LOGIN",font=('Bodoni Bd BT',20),width=0,height=1,bg='#880808',fg='white')
        Loginlbl.place(x=65,y=40)

        user_nm_lbl = Label(loginframe_leftside,text="Enter User Name",font=('century gothic bold',15),bg='#880808',fg='white')
        user_nm_lbl.place(x=65,y=100)

        user_nm_txt = Entry(loginframe_leftside,textvariable=name_var,font=('century gothic',15),width=21,relief='ridge')
        user_nm_txt.place(x=65,y=130)

        user_pwd_lbl = Label(loginframe_leftside,text="Enter Password",font=('century gothic bold',15),bg='#880808',fg='white')
        user_pwd_lbl.place(x=65,y=180)

        user_pwd_txt = Entry(loginframe_leftside,textvariable=passw_var,font=('century gothic',15), width=21,relief='ridge',show='*')
        user_pwd_txt.place(x=65,y=210)

        img = Image.open("images/loginscreen1.png")
        img = ImageTk.PhotoImage(img)
        panel = Label(loginframe_sub, image=img,height=360,width=400,bg='white')
        panel.image = img
        panel.place(x=0,y=150)

        self.heading_lbl = Label(loginframe_sub,text='BOOK MY SHOW',font=('Bodoni Bd BT',30),fg='black',bg='white',width=0,height=1)
        self.heading_lbl.place(x=35,y=50)

        self.heading_lbl = Label(loginframe_sub,text='Your Gateway to Entertainment!',font=('Bodoni Bk BT',12),fg='black',bg='white',width=0,height=1)
        self.heading_lbl.place(x=100,y=100)

        warning_lbl = Label(loginframe_leftside,text="Do must check USER NAME & PASSWORD is correct",font=('century gothic',10),bg='#880808',fg='white')
        warning_lbl.place(x=15,y=370)

class AdminDashboard():
    def _init_(self,window):
        self.window = window
        self.window.title("BOOK MY SHOW")
        self.window.state('zoomed')
        self.window.config(background='white')

        # Sidebar
        self.sidebar = Frame(self.window,bg='#880808')
        self.sidebar.place(x=0,y=0,height=660,width=225)

        self.sidebar_book = Label(self.sidebar,text='BOOK',foreground='white',background='#880808',font=('Bodoni Bd BT',30),width=0,height=1)
        self.sidebar_book.place(x=20,y=500)

        self.sidebar_my = Label(self.sidebar,text='MY',foreground='white',background='#880808',font=('Bodoni Bd BT',30),width=0,height=1)
        self.sidebar_my.place(x=20,y=550)

        self.sidebar_show = Label(self.sidebar,text='SHOW',foreground='white',background='#880808',font=('Bodoni Bd BT',30),width=0,height=1)
        self.sidebar_show.place(x=20,y=600)

        # Header
        self.header = Frame(self.window,bg='#880808')
        self.header.place(x=225,y=0,height=40,width=1060)

        self.headertxt = Label(self.window,text='Your Gateway to Entertainment!',foreground='white',background='#880808',font=('Bodoni Bd BT',15),width=25,height=1)
        self.headertxt.place(x=270,y=5)

        self.versiontxt = Label(self.window,text='Version 1.0',foreground='white',background='#880808',font=("century gothic bold",10),width=8,height=1)
        self.versiontxt.place(x=1170,y=10)

        # Dashboard Button

        DashboardBtn = Button(self.sidebar,text="Dashboard",font=("century gothic bold",10),width=20,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=lambda:MenuSystem(DashboardMenu))
        DashboardBtn.place(x=20,y=50)

        MovieBtn = Button(self.sidebar,text="Movie",font=("century gothic bold",10),width=20,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=lambda:MenuSystem(MovieMenu))
        MovieBtn.place(x=20,y=110)

        TicketBookingBtn = Button(self.sidebar,text="TicketBooking",font=("century gothic bold",10),width=20,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=lambda:MenuSystem(TicketBookingMenu))
        TicketBookingBtn.place(x=20,y=180)

        ViewBookingBtn = Button(self.sidebar,text="ViewBooking",font=("century gothic bold",10),width=20,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=lambda:MenuSystem(ViewBookingMenu))
        ViewBookingBtn.place(x=20,y=250)

        offersBtn = Button(self.sidebar,text="Offer's",font=("century gothic bold",10),width=20,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=lambda:MenuSystem(OfferMenu))
        offersBtn.place(x=20,y=320)

        SettingBtn = Button(self.sidebar,text="Setting",font=("century gothic bold",10),width=20,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=lambda:MenuSystem(SettingMenu))
        SettingBtn.place(x=20,y=390)

        LogoutBtn = Button(self.sidebar,text="LogOut",font=("century gothic bold",10),width=20,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=lambda:MenuSystem(LogoutMenu))
        LogoutBtn.place(x=20,y=460)

        #Function for menu system

        main_frame = Frame(window)
        main_frame.config(background='white',height=620,width=1060)
        main_frame.place(x=225,y=40)

        def MenuSystem(page):
            for frame in main_frame.winfo_children():
                frame.destroy()
            page()

        def DashboardMenu():
            DashboardFrame = Frame(main_frame,background='white')
            DashboardFrame.config(height=620,width=1060)
            DashboardFrame.place(x=0,y=0)

        # Moview Dashboard

        def MovieMenu():
            MovieFrame = Frame(main_frame,background='white')
            MovieFrame.config(height=620,width=1060)
            MovieFrame.place(x=0,y=0)
            
            Movielbl = Label(MovieFrame,background='white',text='MOVIE', font=('century gothic bold',25))
            Movielbl.config(height=1,width=0)
            Movielbl.place(x=80,y=17)

            Movie_Operation1_bar = Frame(MovieFrame,background='#880808')
            Movie_Operation1_bar.config(height=40,width=60)
            Movie_Operation1_bar.place(x=0,y=20)

            Movie_Operation_bar = Frame(MovieFrame,background='#880808')
            Movie_Operation_bar.config(height=40,width=825)
            Movie_Operation_bar.place(x=215,y=20)

            MovieAddBtn = Button(Movie_Operation_bar,text="ADD MOVIE",font=("century gothic bold",12),width=15,height=1,background='#880808',foreground='white',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=MovieCRUD_calling)
            MovieAddBtn.place(x=330,y=1)

            MovieUpdateBtn = Button(Movie_Operation_bar,text="UPDATE MOVIE",font=("century gothic bold",12),width=15,height=1,background='#880808',foreground='white',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=MovieCRUD_calling)
            MovieUpdateBtn.place(x=490,y=1)

            MovieDeleteBtn = Button(Movie_Operation_bar,text="DELETE MOVIE",font=("century gothic bold",12),width=15,height=1,background='#880808',foreground='white',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=MovieCRUD_calling)
            MovieDeleteBtn.place(x=650,y=1)

            MovieComingFrame = Frame(MovieFrame,background='#880808')
            MovieComingFrame.config(height=270,width=1025)
            MovieComingFrame.place(x=15,y=70)

            MovieMrngShow = Frame(MovieFrame,background='#880808')
            MovieMrngShow.config(height=260,width=505)
            MovieMrngShow.place(x=15,y=350)

            Moviemrnglbl = Label(MovieMrngShow,background='#880808',foreground='white',text='MORNING SHOW', font=('century gothic bold',15))
            Moviemrnglbl.config(height=1,width=0)
            Moviemrnglbl.place(x=150,y=10)

            MovieNightShow = Frame(MovieFrame,background='#880808')
            MovieNightShow.config(height=260,width=505)
            MovieNightShow.place(x=535,y=350)

            MovieNightlbl = Label(MovieNightShow,background='#880808',foreground='white',text='NIGHT SHOW', font=('century gothic bold',15))
            MovieNightlbl.config(height=1,width=0)
            MovieNightlbl.place(x=190,y=10)

        #TicketBooking Dashboard
        def TicketBookingMenu():
            TicketBookingFrame = Frame(main_frame,background='white')
            TicketBookingFrame.config(height=620,width=1060)
            TicketBookingFrame.place(x=0,y=0)

        def ViewBookingMenu():
            ViewBookingFrame = Frame(main_frame,background='white')
            ViewBookingFrame.config(height=620,width=1060)
            ViewBookingFrame.place(x=0,y=0)

        def OfferMenu():
            OfferFrame = Frame(main_frame,background='white')
            OfferFrame.config(height=620,width=1060)
            OfferFrame.place(x=0,y=0)

        def SettingMenu():
            SettingFrame = Frame(main_frame,background='white')
            SettingFrame.config(height=620,width=1060)
            SettingFrame.place(x=0,y=0)

        def LogoutMenu():
            self.window.destroy()
            
class MovieCRUD:
    def _init_(self,MovieCRUDwindow):
        self.MovieCRUDwindow = MovieCRUDwindow
        self.MovieCRUDwindow.title("BOOK MY SHOW - ADD UPDATE DELETE MOVIE")
        self.MovieCRUDwindow.geometry("1000x600")
        self.MovieCRUDwindow.state('normal')

        #Variable Declaration
        id_int = int()
        MovieName = StringVar()
        ReleaseDate = StringVar()
        category = StringVar()
        Duration = StringVar()
        Language = StringVar()
        Short_Description = StringVar()
        Formatee = StringVar()

        # CRUD OPERATION FUNCTION
        # INSERT function
        def Movieinsert():
            MovieId = txtid.get()
            MovieName = txtMovieName.get()
            ReleaseDate = txtReleaseDate.get()

            MovieCategory = txtMovieCategory.get()
            MovieDuration = txtMovieDuration.get()
            MovieLanguage = txtMovieLanguage.get()

            ShortDescription = txtShortDescription.get()
            MovieFormate = txtMovieFormate.get()

            if(MovieId=="" or MovieName=="" or ReleaseDate=="" or MovieCategory=="" or MovieDuration=="" or MovieLanguage=="" or ShortDescription=="" or MovieFormate==""):
                messagebox.showinfo("Insert Status","All fields are required")
            else:
                con = MySQLdb.connect(host="localhost", user="root", password="", database="bookmyshow")
                cursor = con.cursor()
                cursor.execute("insert into movie_details values('"+MovieId+"','"+MovieName+"','"+ReleaseDate+"','"+MovieCategory+"','"+MovieDuration+"','"+MovieLanguage+"','"+ShortDescription+"','"+MovieFormate+"')")
                cursor.execute("commit")

                txtid.delete(0,'end')
                txtMovieName.delete(0,'end')
                txtReleaseDate.delete(0,'end')

                txtMovieCategory.delete(0,'end')
                txtMovieDuration.delete(0,'end')
                txtMovieLanguage.delete(0,'end')

                txtShortDescription.delete(0,'end')
                txtMovieFormate.delete(0,'end')
                messagebox.showinfo("INSERT Status","INSERTED SUCCESSFULLY")
                con.close()

        #DELETE OPERATION
        def MovieDelete():
            if(txtid.get() == ""):
                messagebox.showinfo("Delete Status","ID Is Required For Delete Operation")
            else:
                con = MySQLdb.connect(host="localhost", user="root", password="", database="bookmyshow")
                cursor = con.cursor()
                cursor.execute("delete from movie_details where id='"+txtid.get()+"'")
                cursor.execute("commit")

                txtid.delete(0,'end')
                txtMovieName.delete(0,'end')
                txtReleaseDate.delete(0,'end')

                txtMovieCategory.delete(0,'end')
                txtMovieDuration.delete(0,'end')
                txtMovieLanguage.delete(0,'end')

                txtShortDescription.delete(0,'end')
                txtMovieFormate.delete(0,'end')
                messagebox.showinfo("DELETE Status","DELETED SUCCESSFULLY")
                con.close()

        #UPDATE OPERATION
        def MovieUpdate():
            pass
            MovieId = txtid.get()
            MovieName = txtMovieName.get()
            ReleaseDate = txtReleaseDate.get()

            MovieCategory = txtMovieCategory.get()
            MovieDuration = txtMovieDuration.get()
            MovieLanguage = txtMovieLanguage.get()

            ShortDescription = txtShortDescription.get()
            MovieFormate = txtMovieFormate.get()

            if(MovieId=="" or MovieName=="" or ReleaseDate=="" or MovieCategory=="" or MovieDuration=="" or MovieLanguage=="" or ShortDescription=="" or MovieFormate==""):
                messagebox.showinfo("Update Status","All fields are required")
            else:
                con = MySQLdb.connect(host="localhost", user="root", password="", database="bookmyshow")
                cursor = con.cursor()
                cursor.execute("update movie_details set movie_name='"+txtMovieName.get()+"',release_date='"+txtReleaseDate.get()+"',category='"+txtMovieCategory.get()+"',duration='"+txtMovieDuration.get()+"',language='"+txtMovieLanguage.get()+"',short_description='"+txtShortDescription.get()+"',format='"+txtMovieFormate.get()+"' where id='"+txtid.get()+"'")
                cursor.execute("commit")

                txtid.delete(0,'end')
                txtMovieName.delete(0,'end')
                txtReleaseDate.delete(0,'end')

                txtMovieCategory.delete(0,'end')
                txtMovieDuration.delete(0,'end')
                txtMovieLanguage.delete(0,'end')

                txtShortDescription.delete(0,'end')
                txtMovieFormate.delete(0,'end')
                messagebox.showinfo("UPDATE Status","UPDATED SUCCESSFULLY")
                con.close()

        # ALL FIELD's AND FRAME
        CRUDtxtFild = Frame(MovieCRUDwindow,background='#800808')
        CRUDtxtFild.config(height=350,width=1000)
        CRUDtxtFild.place(x=0,y=0)

        CRUDmenu = Frame(CRUDtxtFild,background='white')
        CRUDmenu.config(height=30,width=1000)
        CRUDmenu.place(x=0,y=10)

        MovieAddBtn = Button(CRUDmenu,text="ADD MOVIE",font=("century gothic bold",10),width=15,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=Movieinsert)
        MovieAddBtn.place(x=540,y=0)

        MovieUpdateBtn = Button(CRUDmenu,text="UPDATE MOVIE",font=("century gothic bold",10),width=15,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=MovieUpdate)
        MovieUpdateBtn.place(x=700,y=0)

        MovieDeleteBtn = Button(CRUDmenu,text="DELETE MOVIE",font=("century gothic bold",10),width=15,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=MovieDelete)
        MovieDeleteBtn.place(x=850,y=0)

        MoviewDetails = Label(CRUDmenu,text="  MOVIE DETAIL's  ",font=('century gothic bold',20),background='#880808',foreground='white')
        MoviewDetails.place(x=50,y=0)

        lblid = Label(CRUDtxtFild,text="MOVIE ID :",font=('century gothic bold',15),background='#880808',foreground='white')
        lblid.place(x=50,y=70)

        txtid = Entry(CRUDtxtFild,textvariable=id_int,font=('century gothic',15),width=20,relief='ridge')
        txtid.place(x=50,y=100)

        lblMovieName = Label(CRUDtxtFild,text="MOVIE NAME :",font=('century gothic bold',15),background='#880808',foreground='white')
        lblMovieName.place(x=50,y=150)

        txtMovieName = Entry(CRUDtxtFild,textvariable=MovieName,font=('century gothic',15),width=20,relief='ridge')
        txtMovieName.place(x=50,y=180)

        lblReleaseDate = Label(CRUDtxtFild,text="RELEASE DATE :",font=('century gothic bold',15),background='#880808',foreground='white')
        lblReleaseDate.place(x=50,y=230)

        txtReleaseDate = Entry(CRUDtxtFild,textvariable=ReleaseDate,font=('century gothic',15),width=20,relief='ridge')
        txtReleaseDate.place(x=50,y=260)

        lblMovieCategory = Label(CRUDtxtFild,text="MOVIE CATEGORY :",font=('century gothic bold',15),background='#880808',foreground='white')
        lblMovieCategory.place(x=390,y=70)
        
        txtMovieCategory = Entry(CRUDtxtFild,textvariable=category,font=('century gothic',15),width=20,relief='ridge')
        txtMovieCategory.place(x=390,y=100)

        lblMovieDuration = Label(CRUDtxtFild,text="MOVIE DURATION :",font=('century gothic bold',15),background='#880808',foreground='white')
        lblMovieDuration.place(x=390,y=150)
        
        txtMovieDuration = Entry(CRUDtxtFild,textvariable=Duration,font=('century gothic',15),width=20,relief='ridge')
        txtMovieDuration.place(x=390,y=180)

        lblMovieLanguage = Label(CRUDtxtFild,text="MOVIE LANGUAGE :",font=('century gothic bold',15),background='#880808',foreground='white')
        lblMovieLanguage.place(x=390,y=230)

        txtMovieLanguage = Entry(CRUDtxtFild,textvariable=Language,font=('century gothic',15),width=20,relief='ridge')
        txtMovieLanguage.place(x=390,y=260)

        lblShortDescription = Label(CRUDtxtFild,text="SHORT DESCRIPTION :",font=('century gothic bold',15),background='#880808',foreground='white')
        lblShortDescription.place(x=730,y=70)
        
        txtShortDescription = Entry(CRUDtxtFild,textvariable=Short_Description,font=('century gothic',15),width=20,relief='ridge')
        txtShortDescription.place(x=730,y=100)

        lblMovieimage = Label(CRUDtxtFild,text="MOVIE IMAGE :",font=('century gothic bold',15),background='#880808',foreground='white')
        lblMovieimage.place(x=730,y=150)
        
        txtMovieimage = Entry(CRUDtxtFild,font=('century gothic',15),width=20,relief='ridge')
        txtMovieimage.place(x=730,y=180)

        lblMovieFormat = Label(CRUDtxtFild,text="MOVIE FORMATE :",font=('century gothic bold',15),background='#880808',foreground='white')
        lblMovieFormat.place(x=730,y=230)

        txtMovieFormate = Entry(CRUDtxtFild,textvariable=Formatee,font=('century gothic',15),width=20,relief='ridge')
        txtMovieFormate.place(x=730,y=260)

        #DATAGRID VIEW AND DATA DESIGN       MovieCRUDwindow
        CRUDtxtDatagridView = Frame(MovieCRUDwindow,background='black')
        CRUDtxtDatagridView.config(height=350,width=1000)
        CRUDtxtDatagridView.place(x=0,y=350)

# Movie ADD UPDATE AND DELETE creation
def MovieCRUD_calling():
    MovieCRUDwindow = Tk()
    MovieCRUD(MovieCRUDwindow)
    MovieCRUDwindow.mainloop()

# window creation
def win():
    window = Tk()
    AdminDashboard(window)
    window.mainloop()
 
# LOGIN Main window creation
if _name_ == "_main_":
    loginwindow = Tk()
    app = Login(loginwindow)  # Initialize the Login class
    loginwindow.mainloop()