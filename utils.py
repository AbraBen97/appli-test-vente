import streamlit as st
import random
from data import PRODUITS

@st.cache_data
def charger_image(url):
    return url

def filtrer_produits(categorie, tri, recherche):
    produits = list(PRODUITS.values())
    
    # Filtrer par catégorie
    if categorie != "Tous":
        produits = [p for p in produits if p["categorie"] == categorie]
    
    # Filtrer par recherche
    if recherche:
        produits = [p for p in produits if recherche.lower() in p["nom"].lower() or recherche.lower() in p["description"].lower()]
    
    # Filtrer par tri
    if tri == "Nouveautés":
        produits = [p for p in produits if p.get("nouveau", False)]
    elif tri == "Promotions":
        produits = [p for p in produits if p.get("promotion", False)]
    elif tri == "Prix croissant":
        produits = sorted(produits, key=lambda x: x["prix"])
    elif tri == "Prix décroissant":
        produits = sorted(produits, key=lambda x: x["prix"], reverse=True)
    
    # Mélanger si catégorie "Tous" et aucun tri spécifique
    if categorie == "Tous" and tri == "Par défaut":
        random.shuffle(produits)
    
    return produits