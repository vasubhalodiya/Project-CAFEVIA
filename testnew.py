con = MySQLdb.connect(host="localhost", user="root", password="", database="bookmyshow")
cursor = con.cursor()
cursor.execute("SELECT * FROM movie_details")
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
    movie_name.place(x=10, y=140)

    def fetch_movie_data():
        try:
            # Connect to MySQL
            connection = MySQLdb.connect(
                host="localhost",
                user="root",
                password="",
                database="bookmyshow"
            )
            cursor = connection.cursor()
            query = "SELECT id, image FROM movie_details"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            connection.close()

            return result
        except Exception as e:
            print(f"Error fetching movie data: {e}")
            return []
        
    def display_movie_card(imageframe, movie_data):
        for idx, (id, image_data) in enumerate(movie_data):
            if image_data:
                try:

                    img = Image.open(io.BytesIO(image_data))  
                    img = img.resize((350, 350))             
                    img_tk = ImageTk.PhotoImage(img) 

                    img_label = Label(imageframe, image=img_tk, bg='white')
                    img_label.image = img_tk  
                    img_label.place(x=8, y=8 + (idx * 40)) 
                except Exception as e:
                    print(f"Error displaying image for movie ID {id}: {e}")
            else:
                
                Label(
                    imageframe,
                    text="No Image",
                    bg='#feffe4',
                    fg='red',
                    font=('Century Gothic', 9)
                ).place(x=10, y=10 + (idx * 40)) 

    imageframe = Frame(MovieCard, background="black", width=100, height=100)
    imageframe.place(x=10, y=10)
    movie_data = fetch_movie_data()

    display_movie_card(imageframe, movie_data)


    card_count += 1