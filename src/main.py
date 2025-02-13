from fastapi import FastAPI
import pickle
import pandas as pd 
from data_model import Water

app = FastAPI(
    title="Water Potability Prediction",
    description = "Predicting Water Potability"
)

with open(r"C:\Users\sfg\mlops_practice\Water Quality and Potability_ML_Pipeline\model.pkl", "rb") as f:
    model = pickle.load(f)
    
@app.get("/")
def index():
    return "Welcome to Water Potability Prediction  FastAPI"

@app.post("/predict")
def model_predict(water: Water):
    sample = pd.DataFrame({
        'ph' : [water.ph],
        'Hardness' : [water.Hardness],
        'Solids' : [water.Solids],
        'Chloramines': [water.Chloramines],
        'Sulfate' : [water.Chloramines],
        'Conductivity': [water.Conductivity],
        'Organic_carbon': [water.Organic_carbon],
        'Trihalomethanes':[water.Trihalomethanes],
        'Turbidity': [water.Turbidity]
    })
    predicted_value = model.predict(sample)
    
    if predicted_value ==1:
        return "Water is Consumable"
    else:
        return "water is not Consumable"
    