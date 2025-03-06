import joblib

model_loaded = joblib.load('model.joblib')

def predict( info):

    y_pred_loaded = model_loaded.predict(X_test_scaled)
    return y_pred_loaded