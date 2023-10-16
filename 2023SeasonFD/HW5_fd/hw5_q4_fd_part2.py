
import requests

url = "http://localhost:9696/predict"

customer = {"job": "unknown", "duration": 270, "poutcome": "failure"}
respose = requests.post(url, json=customer).json()


print(respose)