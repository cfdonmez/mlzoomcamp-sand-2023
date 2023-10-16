import pickle

def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('dv.bin')
model = load('model1.bin')

customer = {"job": "retired", "duration": 445, "poutcome": "success"}


def predict_single(customer, dv,model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:,1]
    return y_pred[0]





prediction = predict_single(customer,dv,model)

print('prediction: %.3f' %prediction)