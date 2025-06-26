import streamlit as st
from components import (
    afficher_header, afficher_statistiques, afficher_barre_recherche,
    afficher_fonctionnalites, afficher_filtres, afficher_carte_produit,
    afficher_details_produit, afficher_temoignages, afficher_contact,
    afficher_panier
)
from styles import load_styles
from utils import filtrer_produits
from data import PRODUITS

# Configuration de la page
st.set_page_config(
    page_title="Boutique Élégance | Mode & Style",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Charger les styles
load_styles()

def main():
    if 'categorie_selectionnee' not in st.session_state:
        st.session_state.categorie_selectionnee = "Tous"
    
    if 'produit_selectionne' not in st.session_state:
        st.session_state.produit_selectionne = None
    
    if 'tri_selectionne' not in st.session_state:
        st.session_state.tri_selectionne = "Par défaut"
    
    if 'recherche' not in st.session_state:
        st.session_state.recherche = ""
    
    if st.session_state.produit_selectionne:
        produit = PRODUITS[st.session_state.produit_selectionne]
        afficher_details_produit(produit)
    else:
        afficher_header()
        #afficher_statistiques()
        afficher_barre_recherche()
        afficher_filtres()
        afficher_panier()
        
        produits_filtres = filtrer_produits(
            st.session_state.categorie_selectionnee,
            st.session_state.tri_selectionne,
            st.session_state.recherche
        )
        
        st.markdown("### 🛍️ Nos Produits")
        
        if produits_filtres:
            cols = st.columns([1, 1, 1])
            for i, produit in enumerate(produits_filtres):
                produit_id = [k for k, v in PRODUITS.items() if v == produit][0]
                with cols[i % 3]:
                    afficher_carte_produit(produit, produit_id)
        else:
            st.info("Aucun produit trouvé pour ces critères.")
        
        afficher_temoignages()
        afficher_fonctionnalites()
        afficher_contact()

if __name__ == "__main__":
    main()