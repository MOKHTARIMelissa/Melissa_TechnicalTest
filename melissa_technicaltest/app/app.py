from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os
print("!!!!!!!!!!!!!!!!!", os.getcwd())
sys.path.append(os.getcwd()+"/app")
from model_predictions import model_predict
from utils import InputData 

app = FastAPI()

@app.post("/predict/")
async def predict(input_data: InputData):
    """Construction d'un endpoint pour l'api de /predict

    Args:
        input_data (InputData): L'instance en entrée

    Returns:
        float: la prediction retournée par le modèle en entrée
    """
    prediction = model_predict(input_data)
    return {"prediction": prediction }