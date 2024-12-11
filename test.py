ProductCategorymain_frame = Frame(CoffeeCategory)
# ProductCategorymain_frame.pack(fill="both", expand=True)
ProductCategorymain_frame.place(relx=0, rely=0.08, relwidth=1, relheight=0.66)

Produc_canvas = Canvas(ProductCategorymain_frame)
Produc_canvas.pack(side="left", fill="both", expand=True)
# Produc_canvas.config(width=1020,height=255)

# Create a vertical scrollbar
scrollbar = Scrollbar(ProductCategorymain_frame, orient="vertical", command=Produc_canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the canvas to use the scrollbar
Produc_canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the content
canvas_frame = Frame(Produc_canvas, background=secondary_color)
Produc_canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Bind the canvas to resize the scroll region
def update_scrollregion(event):
    Produc_canvas.configure(scrollregion=Produc_canvas.bbox("all"))

canvas_frame.bind("<Configure>", update_scrollregion)

# Add mousewheel scrolling functionality
def on_mousewheel(event):
    Produc_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

Produc_canvas.bind_all("<MouseWheel>", on_mousewheel)

con = MySQLdb.connect(host="localhost", user="root", password="", database="cafevia")
cursor = con.cursor()
cursor.execute("SELECT * FROM product")
movies = cursor.fetchall()
con.close()

row_frame = None
card_count = 0
for movie_details in movies:
    if card_count % 4 == 0:
        row_frame = Frame(canvas_frame, background="red")
        row_frame.place(relwidth=0.5)
        row_frame.pack(padx=20, pady=10)

    MovieCard = Frame(row_frame, background="green", width=200, height=210)
    MovieCard.grid(row=0, column=card_count % 4, padx=15)

    movie_name = Label(MovieCard, text=movie_details[1], background="white", foreground="black", font=('century gothic bold', 8))
    movie_name.place(x=10, y=40)

    card_count += 1