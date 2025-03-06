from fastapi import FastAPI
from pydantic import BaseModel
from model_predictions import model_predict
from utils import InputData 

app = FastAPI()

@app.post("/predict/")
async def predict(input_data: InputData):
    print("Entry    api_______________________")
    prediction = model_predict(input_data)
    print("prediction____", prediction)
    return {"prediction": prediction }#prediction.tolist()}