def DashboardMenu():
    DashboardFrame = Frame(main_frame, background=secondary_color)
    DashboardFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

    txtDashboard = Label(DashboardFrame, text="Dashboard", bg=secondary_color, fg=primary_color, font=("century gothic bold", 20))
    txtDashboard.place(relx=0.03, rely=0.02)


# Connect to MySQL Database
    def get_db_connection():
        return mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="",
            database="cafevia"
        )

    # Fetch row count for a specific table
    def get_table_row_count(table_name):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            conn.close()
            return row_count
        except mysql.connector.Error as err:
            print(f"Error fetching data from table '{table_name}': {err}")
            return 0  # Return 0 if there's an error (e.g., table doesn't exist)

    # Create a card with dynamic data
    def create_card(frame, title, value, icon_path, x, y):
        card = Frame(frame, background=sidecart_color)
        card.place(relx=x, rely=y, relwidth=0.22, relheight=0.18)

        # Title label
        Label(card, text=title, bg=sidecart_color, fg="black", font=("Arial", 12)).place(relx=0.08, rely=0.25)
        
        # Value label
        Label(card, text=value, bg=sidecart_color, fg="black", font=("Arial", 25, 'bold')).place(relx=0.08, rely=0.45)
        
        # Icon
        try:
            icon = Image.open(icon_path).convert("RGBA")
            # Reduce opacity to 70%
            alpha = icon.getchannel("A")  # Get the alpha channel
            alpha = alpha.point(lambda p: int(p * 0.7))  # Apply 70% opacity
            icon.putalpha(alpha)  # Set the modified alpha channel back to the image
            # Resize and convert to Tkinter-compatible format
            icon = icon.resize((60, 60))
            icon = ImageTk.PhotoImage(icon)
            # Create icon label and set the image
            icon_label = Label(card, image=icon, bg=sidecart_color)
            icon_label.image = icon
            icon_label.place(relx=0.67, rely=0.28, width=60, height=60)
            
        except Exception as e:
            print(f"Error loading icon for {title}: {e}")

    # Cards data dynamically fetched from the database
    cards_data = [
        {"title": "Happy Customers", "table_name": "customers", "icon_path": "images/happycustomer.png"},
        {"title": "All Category", "table_name": "category", "icon_path": "images/category.png"},
        {"title": "All Products", "table_name": "product", "icon_path": "images/product.png"},
        {"title": "Available Tables", "table_name": "tables", "icon_path": "images/tablebook.png"},
        {"title": "All Orders", "table_name": "orders", "icon_path": "images/order.png"},
        {"title": "Total Sales", "value": "$ 10,000", "icon_path": "images/sales.png"},
    ]

    # Constants for layout
    cards_per_row = 4  # Maximum cards per row
    card_width = 0.22  # Width of each card
    card_height = 0.18  # Height of each card
    horizontal_spacing = 0.02  # Spacing between cards
    vertical_spacing = 0.03  # Spacing between rows

    # Starting position for the first card
    start_relx = 0.03
    start_rely = 0.1

    # Loop to create dashboard cards
    for idx, card in enumerate(cards_data):
        # Fetch the row count from the database if it exists
        if 'table_name' in card:
            row_count = get_table_row_count(card["table_name"])
            card["value"] = str(row_count)  # Update the card with the dynamic value
        
        # Calculate relx and rely for dynamic positioning
        col = idx % cards_per_row
        row = idx // cards_per_row

        relx = start_relx + col * (card_width + horizontal_spacing)
        rely = start_rely + row * (card_height + vertical_spacing)

        # Create the card using the create_card function
        create_card(DashboardFrame, card["title"], card["value"], card["icon_path"], relx, rely)