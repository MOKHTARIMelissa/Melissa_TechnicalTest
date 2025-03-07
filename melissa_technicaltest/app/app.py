from utils import InputData
from model_predictions import model_predict
from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os
sys.path.append(os.getcwd()+"/app")

app = FastAPI()


@app.post("/predict/")
async def predict(input_data: InputData):
    """Construction d'un endpoint pour l'api de /predict

    Args:
        input_data (InputData): L'instance en entrée

    Returns:
        float: la prédiction retournée par le modèle en entrée
    """
    prediction = model_predict(input_data)
    return {"prediction": prediction}
