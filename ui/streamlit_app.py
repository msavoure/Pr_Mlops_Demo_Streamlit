import streamlit as st
import requests

# Configurer la page
st.set_page_config(
    page_title="MLOps Demo - Prédiction",
    page_icon="🔮",
    layout="centered"
)

API_URL = "https://wa-mlops-demo-f7h8a3e8hdc2dgdd.francecentral-01.azurewebsites.net/predict"

st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Barre latérale pour les paramètres
st.sidebar.title("Paramètres")
st.sidebar.markdown("Ajustez les valeurs des caractéristiques ci-dessous.")

# Titre principal
st.title("Prédiction avec Machine Learning")
st.write("Ce modèle prédit la catégorie d'une fleur en fonction de ses caractéristiques.")

# Layout des entrées utilisateur
col1, col2 = st.columns(2)

with col1:
    feature1 = st.number_input("📏 Longueur du sépal (cm)", value=5.1, min_value=0.0, step=0.1)
    feature3 = st.number_input("📏 Longueur du pétale (cm)", value=1.4, min_value=0.0, step=0.1)

with col2:
    feature2 = st.number_input("📐 Largeur du sépal (cm)", value=3.5, min_value=0.0, step=0.1)
    feature4 = st.number_input("📐 Largeur du pétale (cm)", value=0.2, min_value=0.0, step=0.1)

# Bouton de prédiction avec spinner de chargement
if st.button("Lancer la prédiction"):
    data = {"features": [feature1, feature2, feature3, feature4]}
    
    with st.spinner("🔄 Prédiction en cours..."):
        try:
            response = requests.post(API_URL, json=data, timeout=5)
            response.raise_for_status()  

            prediction = response.json().get("prediction", "❌ Erreur")
            st.success(f"🌟 **Prédiction du modèle : {prediction}**")
            st.balloons() 

        except requests.exceptions.RequestException as e:
            st.error(f"🚨 Erreur de connexion à l'API : {e}")

# Pied de page
st.markdown("---")
st.markdown("**Projet File Rouge MLOps**")
