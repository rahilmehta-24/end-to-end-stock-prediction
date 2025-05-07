import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(data):
    X = data[['Open', 'High', 'Low', 'Volume']]
    y = data['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    joblib.dump(model, 'models/stock_model.pkl')

if __name__ == "__main__":
    data = pd.read_sql('SELECT * FROM processed_stock_data', 'postgresql://user:password@localhost:5432/stock_db')
    train_model(data)
