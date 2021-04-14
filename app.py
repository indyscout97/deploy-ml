from flask import Flask
from flask import jsonify
from flask import request
import json
import pickle
import numpy as np

with open('model.pkl' , 'rb') as f:
    # pickle the data dictionary using the highest protocol availabe
    pipe = pickle.load(f)

app = Flask(__name__)

# Creating the predict route
@app.route('/predict', methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        the_data = request.get_json(force=True)
        newdata = the_data['newdata']
        newdata = np.array(newdata)
        if newdata.ndim == 1:
            newdata = [newdata]
        else:
            newdata = newdata
        prediction = pipe.predict_proba(newdata)
        pred= prediction[:,1] # saving results from positive class only as this is probability of phishing website
        return {'prediction' : pred.tolist()}
    if request.method == 'GET':
        x = 'This project is still a WIP!!!'
        return x
