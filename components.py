import streamlit as st
from data import PRODUITS, CATEGORIES, TEMOIGNAGES, INFO_BOUTIQUE
from utils import charger_image

def afficher_statistiques():
    st.markdown("""
    <div class="stats-section">
        <h2>📊 Nos Chiffres Qui Parlent</h2>
        <div class="stat-item">
            <span class="stat-number">500+</span>
            <span class="stat-label">Clients Satisfaits</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">1000+</span>
            <span class="stat-label">Vêtements Vendus</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">4.9/5</span>
            <span class="stat-label">Note Moyenne</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">48h</span>
            <span class="stat-label">Livraison Express</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def afficher_barre_recherche():
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col1:
        recherche = st.text_input("🔍 Rechercher un produit...", placeholder="Ex: robe, pantalon, haut...")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 Rechercher", use_container_width=True):
            if recherche:
                st.session_state.recherche = recherche.lower()
            else:
                st.session_state.recherche = ""
    st.markdown('</div>', unsafe_allow_html=True)
    return recherche

def afficher_fonctionnalites():
    st.markdown("""
    <div class="feature-highlight">
        <h2>🌟 Pourquoi Choisir Boutique Élégance ?</h2>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 1.5rem;">
            <div style="margin: 0.8rem; text-align: center;">
                <div style="font-size: 2.5rem;">🎯</div>
                <h4>Qualité Premium</h4>
                <p>Sélection rigoureuse des meilleurs tissus</p>
            </div>
            <div style="margin: 0.8rem; text-align: center;">
                <div style="font-size: 2.5rem;">🚚</div>
                <h4>Livraison Rapide</h4>
                <p>Expédition sous 24h partout en Côte d'Ivoire</p>
            </div>
            <div style="margin: 0.8rem; text-align: center;">
                <div style="font-size: 2.5rem;">💝</div>
                <h4>Service Client</h4>
                <p>Support dédié pour une expérience parfaite</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def afficher_temoignages():
    st.markdown("""
    <div class="feature-highlight">
        <h2>🌟 Ce que nos clients disent</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns([1, 1, 1])
    for i, temoignage in enumerate(TEMOIGNAGES):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="testimonial-card">
                <h4>{temoignage['nom']}</h4>
                <p><b>Produit:</b> {temoignage['produit']}</p>
                <p><b>Note:</b> {'⭐' * temoignage['note']}</p>
                <p>{temoignage['commentaire']}</p>
            </div>
            """, unsafe_allow_html=True)

def afficher_header():
    st.markdown("""
    <div class="promo-banner">
        🎉 OFFRE SPÉCIALE : Livraison gratuite dès 75€ d'achat ! 🚚✨
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="main-header">
        <div class="floating-badge">NOUVEAU</div>
        <h1>✨ Boutique Élégance ✨</h1>
        <p style="font-size: 1.1rem; margin: 0.8rem 0;">Découvrez notre collection de vêtements tendance et élégants</p>
        <p style="font-size: 0.9rem; opacity: 0.9;">🌟 Mode Premium • 🚚 Livraison Rapide • 💎 Qualité Garantie</p>
    </div>
    """, unsafe_allow_html=True)

def afficher_filtres():
    st.markdown('<div class="category-filter">', unsafe_allow_html=True)
    st.markdown("### 🏷️ Catégories")
    
    cols = st.columns(len(CATEGORIES))
    for i, cat in enumerate(CATEGORIES):
        with cols[i]:
            if st.button(cat.title(), key=f"cat_{cat}", use_container_width=True):
                st.session_state.categorie_selectionnee = cat
    
    st.markdown("### 📈 Trier par")
    tri_options = ["Par défaut", "Prix croissant", "Prix décroissant", "Nouveautés", "Promotions"]
    tri_selectionne = st.selectbox("Trier par", tri_options, index=0, key="tri_select")
    st.session_state.tri_selectionne = tri_selectionne
    
    st.markdown('</div>', unsafe_allow_html=True)

def afficher_carte_produit(produit, produit_id):
     with st.container():
         badge_html = ""
         if produit.get("nouveau", False):
             badge_html += '<span class="new-badge">Nouveau</span>'
         if produit.get("promotion", False):
             badge_html += f'<span class="sale-badge">-{int((produit["prix_original"] - produit["prix"]) / produit["prix_original"] * 100)}%</span>'
        
         prix_html = f'<div class="product-price">{produit["prix"]:.2f} €</div>'
         if produit.get("promotion", False):
             prix_html = f'<div class="product-price"><s>{produit["prix_original"]:.2f} €</s> {produit["prix"]:.2f} €</div>'

        
         st.markdown(f"""
         <div class="product-card">
             {badge_html}
             <img src="{charger_image(produit['image_principale'])}" class="product-image" alt="{produit['nom']}">
             <div class="product-title">{produit['nom']}</div>
             <div style="margin: 0.5rem 0;">
                 {"".join([f'<span class="size-badge">{taille}</span>' for taille in produit['tailles']])}
             </div>
             {prix_html}
             
         </div>
         """, unsafe_allow_html=True)
        
         if st.button("Voir les détails", key=f"detail_{produit_id}", use_container_width=True):
             st.session_state.produit_selectionne = produit_id
             st.rerun()



def afficher_details_produit(produit):
    if st.button("← Retour à la boutique", key="back_button"):
        st.session_state.produit_selectionne = None
        st.rerun()
    
    st.markdown('<div class="detail-modal">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"### {produit['nom']}")
        prix_html = f"**Prix:** {produit['prix']:.2f} €"
        if produit.get("promotion", False):
            prix_html = f"**Prix:** <s>{produit['prix_original']:.2f} €</s> {produit['prix']:.2f} €"
        st.markdown(prix_html, unsafe_allow_html=True)
        st.markdown(f"**Catégorie:** {produit['categorie'].title()}")
        
        st.markdown("**Tailles disponibles:**")
        taille_selectionnee = st.selectbox("Choisir une taille", produit['tailles'], key=f"taille_{produit['nom']}")
        
        st.markdown("**Description:**")
        st.write(produit['description'])
        
        if st.button("Ajouter au panier", key=f"add_cart_{produit['nom']}", use_container_width=True):
            if 'panier' not in st.session_state:
                st.session_state.panier = []
            st.session_state.panier.append({
                "id": [k for k, v in PRODUITS.items() if v == produit][0],
                "nom": produit['nom'],
                "taille": taille_selectionnee,
                "prix": produit['prix'],
                "quantite": 1
            })
            st.success(f"{produit['nom']} (Taille: {taille_selectionnee}) ajouté au panier !")
        
        st.markdown("### 📞 Contact pour commande")
        message_whatsapp = f"Bonjour ! Je suis intéressé(e) par le produit : {produit['nom']} - Taille: {taille_selectionnee} - {produit['prix']:.2f} €"
        lien_whatsapp = f"https://wa.me/{INFO_BOUTIQUE['whatsapp']}?text={message_whatsapp.replace(' ', '%20')}"
        
        st.markdown(f"""
        <div class="order-section">
            <h4>🛍️ Passer votre commande</h4>
            <p>Contactez-nous directement pour commander ce produit !</p>
            <a href="{lien_whatsapp}" target="_blank" class="whatsapp-button">
                📱 Commander sur WhatsApp
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📸 Galerie photos")
        st.image(charger_image(produit['image_principale']), caption="Photo principale", use_container_width=True)
        
        st.markdown("**Photos supplémentaires:**")
        cols = st.columns(3)
        for i, img_url in enumerate(produit['images_supplementaires']):
            with cols[i % 3]:
                st.image(charger_image(img_url), caption=f"Photo {i+1}", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def afficher_contact():
    st.markdown("""
    <div class="contact-section">
        <h2>📞 Nous Contacter</h2>
        <p>Votre satisfaction est notre priorité ! N'hésitez pas à nous contacter</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-item">
            <h4>🏪 Boutique</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write(f"**{INFO_BOUTIQUE['nom']}**")
    
    with col2:
        st.markdown("""
        <div class="contact-item">
            <h4>📱 Téléphone</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write(f"**{INFO_BOUTIQUE['telephone']}**")
    
    with col3:
        st.markdown("""
        <div class="contact-item">
            <h4>✉️ Email</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write(f"**{INFO_BOUTIQUE['email']}**")
    
    st.markdown("---")
    st.markdown("### 💬 Contactez-nous sur WhatsApp")
    
    lien_whatsapp = f"https://wa.me/{INFO_BOUTIQUE['whatsapp']}"
    st.markdown(f"""
    <div style="text-align: center; margin: 1.5rem 0;">
        <a href="{lien_whatsapp}" target="_blank" class="whatsapp-button">
            📱 Écrire sur WhatsApp
        </a>
    </div>
    """, unsafe_allow_html=True)

def afficher_panier():
    if 'panier' not in st.session_state or not st.session_state.panier:
        st.info("Votre panier est vide.")
        return
    
    st.markdown('<div class="cart-section">', unsafe_allow_html=True)
    st.markdown("### 🛒 Votre Panier")
    
    total = 0
    panier_message = "Bonjour ! Voici ma commande :\n"
    for item in st.session_state.panier:
        total += item['prix'] * item['quantite']
        panier_message += f"- {item['nom']} (Taille: {item['taille']}, Quantité: {item['quantite']}) : {item['prix']:.2f} €\n"
        
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        with col1:
            st.write(f"**{item['nom']}** (Taille: {item['taille']})")
        with col2:
            st.write(f"{item['prix']:.2f} €")
        with col3:
            quantite = st.number_input("Quantité", min_value=1, value=item['quantite'], key=f"qty_{item['id']}_{item['taille']}")
            item['quantite'] = quantite
        with col4:
            if st.button("Supprimer", key=f"remove_{item['id']}_{item['taille']}"):
                st.session_state.panier = [i for i in st.session_state.panier if not (i['id'] == item['id'] and i['taille'] == item['taille'])]
                st.rerun()
    
    st.markdown(f"**Total:** {total:.2f} €")
    
    panier_message += f"Total: {total:.2f} €"
    lien_whatsapp = f"https://wa.me/{INFO_BOUTIQUE['whatsapp']}?text={panier_message.replace(' ', '%20').replace('\n', '%0A')}"
    
    st.markdown(f"""
    <div class="order-section">
        <h4>🛍️ Finaliser votre commande</h4>
        <a href="{lien_whatsapp}" target="_blank" class="whatsapp-button">
            📱 Commander sur WhatsApp
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Vider le panier", use_container_width=True):
        st.session_state.panier = []
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)