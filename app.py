import flask
from flask import Flask,render_template,request
import numpy as np
import pickle
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
app=Flask(__name__)
with open("SLR_MODEL.pkl","rb") as p:
    model=pickle.load(p)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    values=[float(x) for x in request.form.values()]
    values=np.array(values).reshape(-1,1)
    result=model.predict(values)
    return render_template('index.html',prediction_text=result)
if __name__=='__main__':
    app.run(debug=True)