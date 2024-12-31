con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
cursor = con.cursor()
cursor.execute("SELECT * FROM product")
movies = cursor.fetchall()
con.close()

row_frame = None
card_count = 0
for movie_details in movies:
    if card_count % 4 == 0:
        row_frame = Frame(canvas_frame,background="#880808")
        row_frame.pack(pady=10)

    MovieCard = Frame(row_frame, background="white", width=234, height=220)
    MovieCard.grid(row=0, column=card_count % 4, padx=10)

    movieDetailsBtn = Button(MovieCard,text="DETAILS",font=("century gothic bold",12),width=22,height=1,background='#880808',foreground='white',cursor="hand2",highlightthickness=2,relief="flat",overrelief="raise",activebackground="darkred",bd=3)
    movieDetailsBtn.place(x=10,y=178)

    movie_name = Label(MovieCard, text=movie_details[1], background="white", foreground="black", font=('century gothic bold', 8))
    movie_name.place(x=10, y=150)

    Movie_img_frame = Frame(MovieCard, background="red", width=100, height=100)
    Movie_img_frame.place(x=0,y=0)
    
    card_count += 1