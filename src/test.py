import json
import requests

url = "https://water-potability-prediction-api.onrender.com/predict"
x_new = {
  "ph": 10.71,
  "Hardness": 500.89,
  "Solids": 20791.31,
  "Chloramines": 7.3,
  "Sulfate": 368.51,
  "Conductivity": 564.30,
  "Organic_carbon": 10.37,
   "Trihalomethanes": 86.99,
  "Turbidity": 2.96
}

x_new_json = json.dumps(x_new)

response = requests.post(url, data=x_new_json)
print("Reponse Text: ", response.text)
print("Status Code: ", response.status_code)

    
