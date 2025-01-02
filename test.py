import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

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

def plot_charts(df):
    """Plot all charts in one window with 2 charts per row."""
    # 1. Aggregate product sales for the pie chart
    product_sales = df.groupby('ordername')['total_qty'].sum()

    # 2. Aggregate daily product quantities for the line chart
    daily_sales = df.groupby(['sale_date'])['total_qty'].sum()

    # 3. Aggregate customer orders for the bar chart
    customer_orders = df.groupby(['customername', 'sale_date'])['total_qty'].sum().unstack()

    # Create a figure with two rows and two columns (adjust the grid accordingly)
    fig, axes = plt.subplots(2, 2, figsize=(20, 12))

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
    plt.show()

if __name__ == "__main__":
    # Fetch data
    sales_data = fetch_sales_data()

    if not sales_data.empty:
        # Plot the charts
        plot_charts(sales_data)
    else:
        print("No data found or failed to fetch data.")
