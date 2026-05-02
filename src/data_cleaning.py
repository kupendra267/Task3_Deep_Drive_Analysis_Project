import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

    print("\nFinal Columns:", df.columns)

    # Rename important columns
    df.rename(columns={
        'amount': 'sales'
    }, inplace=True)

    # Remove unwanted columns
    if 'unnamed:_22' in df.columns:
        df.drop(columns=['unnamed:_22'], inplace=True)

    # Convert data types
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

    if 'qty' in df.columns:
        df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

    # Remove nulls & duplicates
    df.dropna(subset=['sales', 'order_id', 'date'], inplace=True)
    df.drop_duplicates(inplace=True)

    print("\nData cleaned successfully!")

    return df