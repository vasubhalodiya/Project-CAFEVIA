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
        SELECT ordername, customername, SUM(orderqty) AS total_qty, SUM(orderprice * orderqty) AS total_sales, DATE(orderdate) AS sale_date
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

def plot_combined_charts(df):
    """Plot all charts in one window."""
    # Pie Chart: Total products sold by product name
    total_qty_by_product = df.groupby('ordername')['total_qty'].sum()

    # Line Chart 1: Date vs Product Quantity
    total_qty_by_date = df.groupby('sale_date')['total_qty'].sum()

    # Line Chart 2: Customer vs Date (Orders Count)
    orders_by_customer_date = df.groupby(['sale_date', 'customername']).size().unstack(fill_value=0)

    # Create a figure with three subplots
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    # Pie chart: Products sold distribution
    axes[0].pie(total_qty_by_product, labels=total_qty_by_product.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
    axes[0].set_title("Product Sales Distribution (in %)")

    # Line chart 1: Date vs Product Quantity
    axes[1].plot(total_qty_by_date.index, total_qty_by_date, marker='o', color='blue', linestyle='-', linewidth=2)
    axes[1].set_title("Date vs Product Quantity")
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel("Total Quantity Sold")
    axes[1].tick_params(axis='x', rotation=45)

    # Line chart 2: Customer vs Date (Order Counts)
    for customer in orders_by_customer_date.columns:
        axes[2].plot(orders_by_customer_date.index, orders_by_customer_date[customer], marker='o', linestyle='-', label=customer)
    axes[2].set_title("Customer vs Date (Order Counts)")
    axes[2].set_xlabel("Date")
    axes[2].set_ylabel("Number of Orders")
    axes[2].tick_params(axis='x', rotation=45)
    axes[2].legend(title="Customer", bbox_to_anchor=(1.05, 1), loc='upper left')

    # Adjust layout
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Fetch data
    sales_data = fetch_sales_data()

    if not sales_data.empty:
        # Plot combined charts
        plot_combined_charts(sales_data)
    else:
        print("No data found or failed to fetch data.")
