import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pickle
import joblib
import config

def train():
    """S'encharge de l'entrainement d'un modèle de regression sur le dataset en entrée
    """
    try:
        dataset = pd.read_excel(config.DATA_PATH)
    except:
        print(f"Erreur: durant l'ouverture du fichier {config.DATA_PATH}")
        print("Verifier le chemin et l'extension du fichier <.xlsx>")
        quit()

    print("Informations à propos des données:")
    print(dataset.info())
    print("__________________")
    print(dataset.describe())
    print("__________________")

    # Prétraitement et normalisation des données:
    labelEncoder = LabelEncoder()
    scaler = StandardScaler()

    X = dataset.drop(columns=["vlm_financial_info (target)"])
    y = dataset["vlm_financial_info (target)"]

    X["asset_building_type_asset"] = labelEncoder.fit_transform(
        X["asset_building_type_asset"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True)

    X_train_norm = scaler.fit_transform(X_train)

    X_test_norm = scaler.transform(X_test)

    # sauvegarder les outils d'encodage et de normalisation pour la prédiction
    with open('tools.pkl', 'wb') as f:
        pickle.dump([labelEncoder, scaler], f)

    model = RandomForestRegressor(n_estimators=500, random_state=42)
    model.fit(X_train_norm, y_train)

    y_pred = model.predict(X_test_norm)

    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae:.2f}")

    # Sauvegarder le modèle entraîné
    joblib.dump(model, 'model.joblib')

if __name__ == "__main__":
    train()