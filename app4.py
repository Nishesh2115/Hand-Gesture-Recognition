#!/usr/bin/env python
# coding: utf-8

# In[12]:


from flask import Flask, jsonify, request
import numpy as np
from sklearn.externals import joblib
import pandas as pd
app4=Flask(__name__)

@app4.route('/index')
def index():
    return flask.render_template('index.html')

@app4.route('/predict',methods=['POST'])
def predict():
    clf=joblib.load('model.pkl')
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = clf.predict(final_features)
    return render_template('index.html',prediction_text="Alphabet is :{}".format(prediction))
    


# In[ ]:




