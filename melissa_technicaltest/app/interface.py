import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import requests 
import json
from utils import InputData

st.title("Prédiction de la valeur financière d'un bien")

st.sidebar.header("Saisir les données")
asset_building_type = st.sidebar.selectbox("Type de bâtiment", ['HAUSSMANIEN', 'STANDARD'])
year_financial_info = st.sidebar.selectbox("Année", [2020, 2021, 2022])
iq_score = st.sidebar.number_input("IQ Score", min_value=0.0, max_value=200.0, step=0.01)
building_quality = st.sidebar.number_input("Qualité du bâtiment", min_value=0.0, max_value=20.0, step=0.01)

# Les autres colonnes mettre ça dans un contenant et les appelé dans la création de l'entrée du api
O2020_W = st.sidebar.number_input("O2020_W", min_value=0.0, step=0.01)
O2020_SD0001 = st.sidebar.number_input("O2020_SD0001", min_value=0.0, step=0.01)
O2020_SD0002 = st.sidebar.number_input("O2020_SD0002", min_value=0.0, step=0.01)
O2020_SD0003 = st.sidebar.number_input("O2020_SD0003", min_value=0.0, step=0.01)
O2020_SD0004 = st.sidebar.number_input("O2020_SD0004", min_value=0.0, step=0.01)
O2020_BS = st.sidebar.number_input("O2020_BS", min_value=0.0, step=0.01)
O2020_SD0005 = st.sidebar.number_input("O2020_SD0005", min_value=0.0, step=0.01)
O2020_SD0006 = st.sidebar.number_input("O2020_SD0006", min_value=0.0, step=0.01)
O2020_SD0007 = st.sidebar.number_input("O2020_SD0007", min_value=0.0, step=0.01)
O2020_SD0008 = st.sidebar.number_input("O2020_SD0008", min_value=0.0, step=0.01)
O2020_L = st.sidebar.number_input("O2020_L", min_value=0.0, step=0.01)
O2020_SD0009 = st.sidebar.number_input("O2020_SD0009", min_value=0.0, step=0.01)
O2020_SD0010 = st.sidebar.number_input("O2020_SD0010", min_value=0.0, step=0.01)
O2020_SD0011 = st.sidebar.number_input("O2020_SD0011", min_value=0.0, step=0.01)



if st.sidebar.button("Faire une prédiction"):
    values=[asset_building_type, year_financial_info, iq_score, building_quality, O2020_W, O2020_SD0001, O2020_SD0002, O2020_SD0003, O2020_SD0004, O2020_BS, O2020_SD0005, O2020_SD0006, O2020_SD0007, O2020_SD0008, O2020_L, O2020_SD0009, O2020_SD0010, O2020_SD0011]
    inputs= InputData(**dict(zip(InputData.__annotations__.keys(), values)))
    print(inputs.get_info())
    req= requests.post(url = "http://app:8000/predict/",     headers={
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }, data = inputs.model_dump_json())
    print(req.json().keys())
    #print(inputs.model_dump_json())
    #prediction = predict() # TODO:ici c'est lapi normalement mais pour le moment on utilise la fct directement
    print(req.json())
    # Afficher la prédiction
    print("blabla")
    st.write(f"La prédiction pour la valeur financière est : {req.json()["prediction"]}")