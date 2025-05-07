import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

def fetch_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def store_data(data, db_url):
    engine = create_engine(db_url)
    data.to_sql('stock_data', engine, if_exists='replace')

if __name__ == "__main__":
    data = fetch_data('AAPL', '2020-01-01', '2023-01-01')
    store_data(data, 'postgresql://user:password@localhost:5432/stock_db')
