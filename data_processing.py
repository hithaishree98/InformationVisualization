# data_processing.py
import pandas as pd

def load_and_process_data(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)

    # Convert 'Date' column to datetime type if not already
    df['Date'] = pd.to_datetime(df['Date'])

    # Set 'Date' as the index
    df.set_index('Date', inplace=True)

    # Add price range (High - Low) and other useful columns
    df['Price Range'] = df['High'] - df['Low']

    # Resample the data by month
    df_resampled = df.resample('M').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum',
        'Price Range': 'mean'
    })

    return df_resampled
