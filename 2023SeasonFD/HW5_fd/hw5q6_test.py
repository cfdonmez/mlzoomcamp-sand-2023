
import requests

url = "http://localhost:9696/predict"

customer = {"job": "retired", "duration": 445, "poutcome": "success"}
respose = requests.post(url, json=customer).json()

print(respose)