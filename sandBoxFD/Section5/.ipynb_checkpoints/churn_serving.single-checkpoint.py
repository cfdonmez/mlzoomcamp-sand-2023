{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "14481fab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "prediction: 0.062\n",
      "verdict: Not churn\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "def predict_single(customer, dv, model):\n",
    "    X = dv.transform([customer])\n",
    "    y_pred = model.predict_proba(X)[:, 1]\n",
    "    return y_pred[0]\n",
    "\n",
    "\n",
    "with open('model_C=1.0.bin', 'rb') as f_in:\n",
    "    dv, model = pickle.load(f_in)\n",
    "\n",
    "\n",
    "customer = {\n",
    "    'customerid': '8879-zkjof',\n",
    "    'gender': 'female',\n",
    "    'seniorcitizen': 0,\n",
    "    'partner': 'no',\n",
    "    'dependents': 'no',\n",
    "    'tenure': 41,\n",
    "    'phoneservice': 'yes',\n",
    "    'multiplelines': 'no',\n",
    "    'internetservice': 'dsl',\n",
    "    'onlinesecurity': 'yes',\n",
    "    'onlinebackup': 'no',\n",
    "    'deviceprotection': 'yes',\n",
    "    'techsupport': 'yes',\n",
    "    'streamingtv': 'yes',\n",
    "    'streamingmovies': 'yes',\n",
    "    'contract': 'one_year',\n",
    "    'paperlessbilling': 'yes',\n",
    "    'paymentmethod': 'bank_transfer_(automatic)',\n",
    "    'monthlycharges': 79.85,\n",
    "    'totalcharges': 3320.75,\n",
    "}\n",
    "    \n",
    "\n",
    "prediction = predict_single(customer, dv, model)\n",
    "\n",
    "print('prediction: %.3f' % prediction)\n",
    "\n",
    "if prediction >= 0.5:\n",
    "    print('verdict: Churn')\n",
    "else:\n",
    "    print('verdict: Not churn')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6eb3cfbc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.17"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
