import pandas as pd

def preprocess_data(data):
    data.dropna(inplace=True)
    data['MA50'] = data['Close'].rolling(window=50).mean()
    return data

if __name__ == "__main__":
    data = pd.read_sql('SELECT * FROM stock_data', 'postgresql://user:password@localhost:5432/stock_db')
    processed_data = preprocess_data(data)
    processed_data.to_sql('processed_stock_data', 'postgresql://user:password@localhost:5432/stock_db', if_exists='replace')
