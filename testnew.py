from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd


def fetch_sales_data():
    """Fetch sales data from the MySQL database."""
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cafevia"
        )

        # Query to fetch sales data
        query = """
        SELECT ordername, customername, SUM(orderqty) AS total_qty, SUM(orderprice * orderqty) AS total_sales,
            DATE(orderdate) AS sale_date
        FROM orders
        GROUP BY ordername, customername, sale_date
        """

        # Load data into a pandas DataFrame
        df = pd.read_sql(query, conn)
        return df

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return pd.DataFrame()

    finally:
        if conn.is_connected():
            conn.close()


def plot_charts(df, parent_frame):
    """Plot all charts in one frame using Tkinter canvas."""
    # 1. Aggregate product sales for the pie chart
    product_sales = df.groupby('ordername')['total_qty'].sum()

    # 2. Aggregate daily product quantities for the line chart
    daily_sales = df.groupby(['sale_date'])['total_qty'].sum()

    # 3. Aggregate customer orders for the bar chart
    customer_orders = df.groupby(['customername', 'sale_date'])['total_qty'].sum().unstack()

    # Create a figure with two rows and two columns
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Pie Chart - Product Sales Percentage (top-left)
    axes[0, 0].pie(product_sales, labels=product_sales.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
    axes[0, 0].set_title("Product Sales Percentage")

    # Line Chart - Daily Product Sales (top-right)
    axes[0, 1].plot(daily_sales.index, daily_sales, marker='o', color='blue', linestyle='-', linewidth=2)
    axes[0, 1].set_title("Daily Product Sales")
    axes[0, 1].set_xlabel("Date")
    axes[0, 1].set_ylabel("Total Quantity Sold")
    axes[0, 1].tick_params(axis='x', rotation=45)

    # Bar Chart - Orders by Customer and Date (bottom-left)
    customer_orders.T.plot(kind='bar', stacked=True, ax=axes[1, 0], colormap='tab20')
    axes[1, 0].set_title("Orders by Customer and Date")
    axes[1, 0].set_xlabel("Date")
    axes[1, 0].set_ylabel("Number of Products Sold")
    axes[1, 0].legend(title="Customer", bbox_to_anchor=(1.05, 1), loc='upper left')
    axes[1, 0].tick_params(axis='x', rotation=45)

    # Empty plot for bottom-right (you can add another chart here if needed)
    axes[1, 1].axis('off')

    # Adjust layout
    plt.tight_layout()

    # Embed the figure in the Tkinter frame
    canvas = FigureCanvasTkAgg(fig, parent_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=BOTH, expand=True)
    canvas.draw()


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")

    # Main frame setup
    main_frame = Frame(root, background="gray")
    main_frame.pack(fill=BOTH, expand=True)

    # SalesFrame setup
    SalesFrame = Frame(main_frame, background='darkred')
    SalesFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Fetch and display data
    sales_data = fetch_sales_data()
    if not sales_data.empty:
        plot_charts(sales_data, SalesFrame)
    else:
        Label(SalesFrame, text="No data found or failed to fetch data.", bg='darkred', fg='white', font=("Arial", 14)).pack(pady=20)

    root.mainloop()
