import matplotlib.pyplot as plt
import os

def plot_charts(region_sales, category_sales, monthly_sales):

    os.makedirs("outputs/charts", exist_ok=True)

    # ✅ Category Sales
    plt.figure()
    plt.bar(category_sales['category'], category_sales['sales'])
    plt.title("Sales by Category")
    plt.xticks(rotation=45)
    plt.savefig("outputs/charts/category_sales.png")

    # ✅ Monthly Sales
    plt.figure()
    plt.plot(monthly_sales['month'].astype(str), monthly_sales['sales'])
    plt.title("Monthly Sales Trend")
    plt.xticks(rotation=45)
    plt.savefig("outputs/charts/monthly_sales.png")

    # ✅ Region Sales
    plt.figure()
    plt.pie(region_sales['sales'], labels=region_sales['ship_state'], autopct='%1.1f%%')
    plt.title("Sales by State")
    plt.savefig("outputs/charts/region_sales.png")