# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:01:17 2020

"""


import sklearn. linear_model.LogisticRegression as LogisticRegression
import pandas as pd
import streamlit as st 
#from sklearn.linear_model import LogisticRegression
import pickle.dump as dump
import pickle.load as load

st.title('Model Deployment: pre- built Logistic Regression')

st.sidebar.header('User Input Parameters')

def user_input_features():
    CLMSEX = st.sidebar.selectbox('Gender',('1','0'))
    CLMINSUR = st.sidebar.selectbox('Insurance',('1','0'))
    SEATBELT = st.sidebar.selectbox('SeatBelt',('1','0'))
    CLMAGE = st.sidebar.number_input("Insert the Age")
    LOSS = st.sidebar.number_input("Insert Loss")
    data = {'CLMSEX':CLMSEX,
            'CLMINSUR':CLMINSUR,
            'SEATBELT':SEATBELT,
            'CLMAGE':CLMAGE,
            'LOSS':LOSS}
    features = pd.DataFrame(data,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)


# load the model from disk
loaded_model = load(open('Logistic_Model.sav', 'rb'))

prediction = loaded_model.predict(df)
prediction_proba = loaded_model.predict_proba(df)

st.subheader('Predicted Result')
st.write('Yes, claimant will hire an attorney' if prediction[0]==0 else 'claimant will not hire')

st.subheader('Prediction Probability')
st.write(prediction_proba)


