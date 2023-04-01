from flask import render_template,Flask,request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictData',methods=['GET','POST'])
def predict_data():
    if(request.method=='GET'):
        return render_template('home.html')
    
    else:
        data = CustomData()


