def analyze_data(df):
    # ✅ FIXED: use ship_state instead of region
    region_sales = df.groupby('ship_state')['sales'].sum().reset_index()

    # Category analysis
    category_sales = df.groupby('category')['sales'].sum().reset_index()

    # Monthly analysis
    df['month'] = df['date'].dt.to_period('M')
    monthly_sales = df.groupby('month')['sales'].sum().reset_index()

    return region_sales, category_sales, monthly_sales