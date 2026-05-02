def calculate_kpis(df):
    total_revenue = df['sales'].sum()
    total_orders = df['order_id'].nunique()
    aov = total_revenue / total_orders

    return {
        "Total Revenue": total_revenue,
        "Total Orders": total_orders,
        "AOV": aov
    }