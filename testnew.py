from tkinter import *
from PIL import Image, ImageTk

# Sample data for dashboard cards
cards_data = [
    {
        "title": "Happy Customer",
        "value": "300",
        "icon_path": "images/happycustomer.png",
    },
    {
        "title": "New Orders",
        "value": "120",
        "icon_path": "images/neworders.png",
    },
    {
        "title": "Revenue",
        "value": "$15K",
        "icon_path": "images/revenue.png",
    },
    {
        "title": "Feedbacks",
        "value": "89",
        "icon_path": "images/feedback.png",
    },
]

# Colors
sidecart_color = "#f0f0f0"
primary_color = "#007BFF"

# Initialize root and frame
root = Tk()
root.geometry("800x600")
DashboardFrame = Frame(root, background="white")
DashboardFrame.pack(fill=BOTH, expand=True)

# Loop through card data and create cards
for idx, card in enumerate(cards_data):
    # Create the card frame
    DashboardCard = Frame(DashboardFrame, background=sidecart_color)
    DashboardCard.place(relx=0.03 + idx * 0.25, rely=0.1, relwidth=0.23, relheight=0.19)

    # Add the title label
    lblDashboardCustomer = Label(
        DashboardCard,
        text=card["title"],
        bg=sidecart_color,
        fg=primary_color,
        font=("century gothic", 10),
    )
    lblDashboardCustomer.place(relx=0.07, rely=0.25)

    # Add the value label
    NoDashboardCustomer = Label(
        DashboardCard,
        text=card["value"],
        bg=sidecart_color,
        fg=primary_color,
        font=("century gothic bold", 20),
    )
    NoDashboardCustomer.place(relx=0.07, rely=0.45)

    # Add the icon
    dashboardIcon = Image.open(card["icon_path"]).resize((50, 50))
    dashboardIcon = ImageTk.PhotoImage(dashboardIcon)
    dashboardIcon_label = Label(DashboardCard, image=dashboardIcon, background=sidecart_color)
    dashboardIcon_label.image = dashboardIcon
    dashboardIcon_label.place(relx=0.65, rely=0.28, width=60, height=60)

root.mainloop()
