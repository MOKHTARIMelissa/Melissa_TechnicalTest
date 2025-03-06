import joblib
import pickle
from pydantic import BaseModel
import numpy as np
from utils import InputData

print("appel fonction !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
model_loaded = joblib.load('model.joblib')

with open('tools.pkl', 'rb') as f:
    labelEncoder, scaler = pickle.load(f)

def model_predict(input_data: InputData):
    print("Entry predict_________________________________")
    print(input_data.data_wrap())
    data = input_data.data_wrap()#[[value] for value in input_data]
    data[0]=labelEncoder.transform(data[0])
    y_pred_loaded = model_loaded.predict(scaler.transform(np.array(data).reshape(1, -1)))
    return y_pred_loaded[0]

# TODO: delete this
if __name__=="__main__":
    obj=["HAUSSMANIEN",2020, 831.71, 16.59, 17.28, 8.34, 8.89, 9.14, 9.36, 15.88, 7.56, 6.97, 8.20, 9.75, 16.72, 9.58, 7.08, 8.54]
    
    print(predict(obj))