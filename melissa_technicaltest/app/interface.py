import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import requests 
from utils import InputData

st.title("Prédiction de la valeur financière d'un bien")
asset_building_type = st.selectbox("Type de bâtiment", ['HAUSSMANIEN', 'STANDARD'])
year_financial_info = st.selectbox("Année", [2017, 2018, 2019, 2020, 2021, 2022])
iq_score = st.number_input("IQ Score", min_value=0.0, max_value=200.0, step=0.01)
building_quality = st.number_input("Qualité du bâtiment", min_value=0.0, max_value=20.0, step=0.01)

# Les autres entrées sont placées dans un conteneur
st.subheader("Données supplémentaires pour 2020")

# Entrées pour les autres variables
O2020_W = st.number_input("O2020_W", min_value=0.0, step=0.01)
O2020_SD0001 = st.number_input("O2020_SD0001", min_value=0.0, max_value=20.0, step=0.01)
O2020_SD0002 = st.number_input("O2020_SD0002", min_value=0.0, max_value=20.0, step=0.01)
O2020_SD0003 = st.number_input("O2020_SD0003", min_value=0.0, max_value=20.0, step=0.01)
O2020_SD0004 = st.number_input("O2020_SD0004", min_value=0.0, max_value=20.0, step=0.01)
O2020_BS = st.number_input("O2020_BS", min_value=0.0, max_value=20.0, step=0.01)
O2020_SD0005 = st.number_input("O2020_SD0005", min_value=0.0, max_value=20.0, step=0.01)
O2020_SD0006 = st.number_input("O2020_SD0006", min_value=0.0, max_value=20.0, step=0.01)
O2020_SD0007 = st.number_input("O2020_SD0007", min_value=0.0, max_value=20.0, step=0.01)
O2020_SD0008 = st.number_input("O2020_SD0008", min_value=0.0, max_value=20.0, step=0.01)
O2020_L = st.number_input("O2020_L", min_value=0.0, max_value=20.0, step=0.01)
O2020_SD0009 = st.number_input("O2020_SD0009", max_value=20.0, min_value=0.0, step=0.01)
O2020_SD0010 = st.number_input("O2020_SD0010", max_value=20.0, min_value=0.0, step=0.01)
O2020_SD0011 = st.number_input("O2020_SD0011", max_value=20.0, min_value=0.0, step=0.01)



if st.button("Faire une prédiction"):
    # Transformer la donnée récupérée en la forme voulue
    values=[asset_building_type, year_financial_info, iq_score, building_quality, O2020_W, O2020_SD0001, O2020_SD0002, O2020_SD0003, O2020_SD0004, O2020_BS, O2020_SD0005, O2020_SD0006, O2020_SD0007, O2020_SD0008, O2020_L, O2020_SD0009, O2020_SD0010, O2020_SD0011]
    inputs= InputData(**dict(zip(InputData.__annotations__.keys(), values)))

    # Faire l'appel à l'api chargé de la prédiction
    try:
        req= requests.post(url = "http://0.0.0.0:8000/predict/",     headers={
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }, data = inputs.model_dump_json())
    except: 
        print("Erreur: avec l'appel api revoir l'url")
    
    # Verification du status
    if req.status_code != 200:
        print("Erreur: la requete api a échoué")
        print(f"status code{req.status_code}")

    # Afficher la prédiction
    st.write(f"La prédiction pour la valeur financière du bien est: **{req.json()["prediction"]}**")