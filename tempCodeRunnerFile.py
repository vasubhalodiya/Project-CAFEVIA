#Variable Declaration
        # id_int = int()
        # MovieName = StringVar()
        # ReleaseDate = StringVar()
        # category = StringVar()
        # Duration = StringVar()
        # Language = StringVar()
        # Short_Description = StringVar()
        # Formatee = StringVar()

        # # CRUD OPERATION FUNCTION
        # # INSERT function
        # def Movieinsert():
        #     MovieId = txtid.get()
        #     MovieName = txtMovieName.get()
        #     ReleaseDate = txtReleaseDate.get()

        #     MovieCategory = txtMovieCategory.get()
        #     MovieDuration = txtMovieDuration.get()
        #     MovieLanguage = txtMovieLanguage.get()

        #     ShortDescription = txtShortDescription.get()
        #     MovieFormate = txtMovieFormate.get()

        #     if(MovieId=="" or MovieName=="" or ReleaseDate=="" or MovieCategory=="" or MovieDuration=="" or MovieLanguage=="" or ShortDescription=="" or MovieFormate==""):
        #         messagebox.showinfo("Insert Status","All fields are required")
        #     else:
        #         con = MySQLdb.connect(host="localhost", user="root", password="", database="bookmyshow")
        #         cursor = con.cursor()
        #         cursor.execute("insert into movie_details values('"+MovieId+"','"+MovieName+"','"+ReleaseDate+"','"+MovieCategory+"','"+MovieDuration+"','"+MovieLanguage+"','"+ShortDescription+"','"+MovieFormate+"')")
        #         cursor.execute("commit")

        #         txtid.delete(0,'end')
        #         txtMovieName.delete(0,'end')
        #         txtReleaseDate.delete(0,'end')

        #         txtMovieCategory.delete(0,'end')
        #         txtMovieDuration.delete(0,'end')
        #         txtMovieLanguage.delete(0,'end')

        #         txtShortDescription.delete(0,'end')
        #         txtMovieFormate.delete(0,'end')
        #         messagebox.showinfo("INSERT Status","INSERTED SUCCESSFULLY")
        #         con.close()

        # # ALL FIELD's AND FRAME
        # CRUDtxtFild = Frame(MovieCRUDwindow,background='#800808')
        # CRUDtxtFild.config(height=350,width=1000)
        # CRUDtxtFild.place(x=0,y=0)

        # CRUDmenu = Frame(CRUDtxtFild,background='white')
        # CRUDmenu.config(height=30,width=1000)
        # CRUDmenu.place(x=0,y=10)

        # MovieAddBtn = Button(CRUDmenu,text="ADD MOVIE",font=("century gothic bold",10),width=15,height=1,background='white',foreground='black',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3,command=Movieinsert)
        # MovieAddBtn.place(x=540,y=0)

        # MoviewDetails = Label(CRUDmenu,text="  MOVIE DETAIL's  ",font=('century gothic bold',20),background='#880808',foreground='white')
        # MoviewDetails.place(x=50,y=0)

        # lblid = Label(CRUDtxtFild,text="MOVIE ID :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblid.place(x=50,y=70)

        # txtid = Entry(CRUDtxtFild,textvariable=id_int,font=('century gothic',15),width=20,relief='ridge')
        # txtid.place(x=50,y=100)

        # lblMovieName = Label(CRUDtxtFild,text="MOVIE NAME :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieName.place(x=50,y=150)

        # txtMovieName = Entry(CRUDtxtFild,textvariable=MovieName,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieName.place(x=50,y=180)

        # lblReleaseDate = Label(CRUDtxtFild,text="RELEASE DATE :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblReleaseDate.place(x=50,y=230)

        # txtReleaseDate = Entry(CRUDtxtFild,textvariable=ReleaseDate,font=('century gothic',15),width=20,relief='ridge')
        # txtReleaseDate.place(x=50,y=260)

        # lblMovieCategory = Label(CRUDtxtFild,text="MOVIE CATEGORY :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieCategory.place(x=390,y=70)
        
        # txtMovieCategory = Entry(CRUDtxtFild,textvariable=category,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieCategory.place(x=390,y=100)

        # lblMovieDuration = Label(CRUDtxtFild,text="MOVIE DURATION :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieDuration.place(x=390,y=150)
        
        # txtMovieDuration = Entry(CRUDtxtFild,textvariable=Duration,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieDuration.place(x=390,y=180)

        # lblMovieLanguage = Label(CRUDtxtFild,text="MOVIE LANGUAGE :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieLanguage.place(x=390,y=230)

        # txtMovieLanguage = Entry(CRUDtxtFild,textvariable=Language,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieLanguage.place(x=390,y=260)

        # lblShortDescription = Label(CRUDtxtFild,text="SHORT DESCRIPTION :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblShortDescription.place(x=730,y=70)
        
        # txtShortDescription = Entry(CRUDtxtFild,textvariable=Short_Description,font=('century gothic',15),width=20,relief='ridge')
        # txtShortDescription.place(x=730,y=100)

        # lblMovieimage = Label(CRUDtxtFild,text="MOVIE IMAGE :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieimage.place(x=730,y=150)
        
        # txtMovieimage = Entry(CRUDtxtFild,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieimage.place(x=730,y=180)

        # lblMovieFormat = Label(CRUDtxtFild,text="MOVIE FORMATE :",font=('century gothic bold',15),background='#880808',foreground='white')
        # lblMovieFormat.place(x=730,y=230)

        # txtMovieFormate = Entry(CRUDtxtFild,textvariable=Formatee,font=('century gothic',15),width=20,relief='ridge')
        # txtMovieFormate.place(x=730,y=260)

        # #DATAGRID VIEW AND DATA DESIGN       MovieCRUDwindow
        # CRUDtxtDatagridView = Frame(MovieCRUDwindow,background='black')
        # CRUDtxtDatagridView.config(height=350,width=1000)
        # CRUDtxtDatagridView.place(x=0,y=350)


