import joblib
import pickle
from pydantic import BaseModel
import numpy as np
from utils import InputData

# Loading the model and the tools for encoding and normalizing
model_loaded = joblib.load('model.joblib')

with open('tools.pkl', 'rb') as f:
    labelEncoder, scaler = pickle.load(f)


def model_predict(input_data: InputData):
    """Cette fonction appelle le modèle déjà préentrainé pour faire la prédiction sur les données en entrée

    Args:
        input_data (InputData): La donnée en entrée

    Returns:
        float: la prédiction de la valeur financière du bien
    """
    data = input_data.data_wrap()
    data[0]=labelEncoder.transform(data[0])
    y_pred_loaded = model_loaded.predict(scaler.transform(np.array(data).reshape(1, -1)))
    return y_pred_loaded[0]
