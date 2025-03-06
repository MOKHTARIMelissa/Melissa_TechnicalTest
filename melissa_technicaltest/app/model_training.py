import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pickle

dataset= pd.read_excel("../train_data_IVDS.xlsx")
print(dataset.info())
print("__________________")
print(dataset.describe())
print("__________________")

X = dataset.drop(columns=["vlm_financial_info (target)"])  
y = dataset["vlm_financial_info (target)"]
labelEncoder=LabelEncoder()
X["asset_building_type_asset"] = labelEncoder.fit_transform(X["asset_building_type_asset"])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

scaler = StandardScaler()

X_train_norm = scaler.fit_transform(X_train)

X_test_norm = scaler.transform(X_test)

with open('tools.pkl', 'wb') as f:
    pickle.dump([labelEncoder, scaler], f)

model = RandomForestRegressor(n_estimators=500, random_state=42)#LinearRegression()
model.fit(X_train_norm, y_train)

y_pred = model.predict(X_test_norm)

mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.2f}")

import joblib

# Sauvegarder le modèle entraîné
joblib.dump(model, 'model.joblib')