import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load data
df = pd.read_csv("car_data.csv")

# Convert Fuel_Type (text → number)
df['Fuel_Type'] = df['Fuel_Type'].map({
    'Petrol': 0,
    'Diesel': 1,
    'CNG': 2
})

# Features & Target
X = df[['Year', 'Driven_kms', 'Fuel_Type']]
y = df['Selling_Price']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
pickle.dump(model, open('car_price_model.pkl', 'wb'))

print("✅ Model trained & saved")
