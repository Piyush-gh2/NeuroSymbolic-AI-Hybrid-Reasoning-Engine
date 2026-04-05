import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_model():
    data = pd.read_csv("business_data.csv")
    
    X = data[["marketing_spend", "operations_cost"]]
    y = data["revenue"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

def predict(marketing, operations):
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)
    
    prediction = model.predict([[marketing, operations]])
    return prediction[0]