import streamlit as st
import numpy as np

import pickle as pkl
import os
import warnings
warnings.warn('ignore')

import asyncio

async def scaling(input):
    directory = 'CleanDataset/scaler.pkl'
    scaler = pkl.load(open(directory, 'rb'))
    input = np.reshape(input, (1, 13))
    dataScaled = scaler.transform(input)
    return dataScaled

def load_model(model):
    loaded_model = pkl.load(open(f'Model/{model}.pkl', 'rb'))
    return loaded_model

async def exec_pred(model, data):
    prediction = np.round(model.predict(data), 0)
    return prediction


async def run_ml():
    st.subheader('Song Popularity Prediction')

    st.subheader('Input Your Data')
    Model = st.selectbox('ML Model', 
                         ['AdaBoostRegressor',
                          'GradientBoostingRegressor',
                          'LGBMRegressor',
                          'LinearRegression',
                          'RandomForest',
                          'XGBoost'])
    Duration = st.number_input("Song Duration (ms)", 90000, 335000)
    Acoustic =st.number_input('Acousticness', 0.0, 1.0)
    Dance = st.number_input('Danceability', 0.0, 1.0)
    Energy = st.number_input('Energy', 0.0, 1.0)
    Instrument = st.number_input("Instrumentalness", 0.0, 1.0)
    Key = st.number_input('Key (Pitch Class)', 0, 11)
    Live = st.number_input('Liveness', 0.0, 1.0)
    Loud = st.number_input('Loudness', -39.0, 1.5)
    AudioMode = st.radio('Audio Mode', [0, 1])
    Speech = st.number_input('Speechiness', 0.0, 1.0)
    Tempo = st.number_input('Tempo', 0.0, 240.0)
    TimeSignature = st.selectbox('Time Signature', 
                                 [0, 1, 2, 3, 4, 5])
    AudioValence = st.number_input("Audio Valence", 0.0, 1.0)
    
    with st.expander("Your Selected Options"):
        result = {
            'Duration': Duration,
            'Acoustic': Acoustic,
            'Dance': Dance,
            'Energy': Energy,
            'Instrument': Instrument,
            'Key': Key,
            'Live': Live,
            'Loud': Loud,
            'AudioMode': AudioMode,
            'Speech': Speech,
            'Tempo': Tempo,
            'TimeSignature': TimeSignature,
            'AudioValence': AudioValence
        }
    st.write(result)

    UserInput = []
    for i in result.values():
        UserInput.append(i)
    
    dataScaled = await scaling(UserInput)
    st.write(dataScaled)

    st.subheader("Prediction Result")

    model = load_model(Model)
    prediction = await exec_pred(model, dataScaled)
    st.write(prediction)
    