import pickle
import numpy as np
def predict_single(customer, dv,model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:,1]
    return y_pred[0]

model_file = 'model_C=1.0.bin'
with open(model_file, 'rb') as f_in:
    (dv,model) = pickle.load(f_in)
    #do stuff
    
#do stuffff

customer = {"customer_id": "8879-zkjof","tenure": 41,
 "monthlycharges": 79.85,
 "totalcharges": 3320.75,
 "gender": "female",
 "seniorcitizen":0,
 "partner": "no",
 "dependents": "no",
 "phoneservice": "yes",
 "multiplelines": "no",
 "internetservice": "dsl",
 "onlinesecurity": "yes",
 "onlinebackup": "no",
 "deviceprotection": "yes",
 "techsupport": "yes",
 "streamingtv": "yes",
 "streamingmovies": "yes",
 "contract": "one_year",
 "paperlessbilling": "yes",
 "paymentmethod": "bank_transfer_(automatic)"}

prediction = predict_single(customer,dv,model)
print('prediction: %.3f' %prediction) 