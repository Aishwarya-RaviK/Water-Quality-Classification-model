import pandas as pd
import numpy as np
import streamlit as st
import pickle 

loaded_model=pickle.load(open("C:/Users/ASUS/Downloads/classification_model (2).sav","rb"))

def quality_prediction(input_data):
    input_data=np.asarray(input_data)
    input_data_reshape=input_data.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshape)
    print(prediction)
    if(prediction[0]==0):
        return "The water is non-potable"
    else:
        return "The water is potable"



def main():
    st.title('Water Quality Checker App')

    Ph=st.text_input('Ph value of water')
    Hardness=st.text_input('Hardness')
    Solids=st.text_input('Solids')
    Chloramines=st.text_input('Chloramines')
    Sulfate=st.text_input('Sulfate')
    Conductivity=st.text_input('Conductivity')
    Organic_carbon=st.text_input('Organic carbon')
    Trihalomethanes=st.text_input('Trihalomethanes')
    Turbidity=st.text_input('Turbidity')

    quality_prediction=" "

    if st.button('Quality check result'):
        quality_prediction=quality_prediction([Ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])

    st.success(quality_prediction)

if __name__ == '__main__':
    main()