# app.py

import streamlit as st
from utils import parser, gpt_generation, match_skills, cv_builder

st.set_page_config(page_title="Adaptateur de CV IA", layout="wide")
st.title("Adaptateur de CV intelligent")

# Choix du mode en haut de page
offline_mode = st.sidebar.checkbox("🛠️ Mode hors ligne (mock)", value=False)

tabs = st.tabs([
    "1. Générer un CV adapté",
    "2. Générer une lettre de motivation",
    "3. Résumé et alignement des compétences",
    "4. Optimisation du wording"
])

# Onglet 1 : Génération de CV adapté
with tabs[0]:
    st.header("Génération d’un CV optimisé")
    uploaded_cv = st.file_uploader("Charger votre CV (PDF ou DOCX)", type=["pdf", "docx"], key="cv1")
    uploaded_offer = st.file_uploader("Charger l’offre d’emploi (PDF, DOCX ou texte)", type=["pdf", "docx", "txt"], key="offre1")
    if uploaded_cv and uploaded_offer:
        cv_text = parser.extract_text(uploaded_cv)
        offer_text = parser.extract_text(uploaded_offer)
        generated_cv = gpt_generation.generate_adapted_cv(cv_text, offer_text, offline=offline_mode)
        st.text_area("Aperçu du CV généré", generated_cv, height=400)
        st.download_button("Télécharger le CV", generated_cv, file_name="cv_adapte.txt")

# Onglet 2 : Lettre de motivation
with tabs[1]:
    st.header("Lettre de motivation personnalisée")
    uploaded_cv2 = st.file_uploader("Charger votre CV", type=["pdf", "docx"], key="cv2")
    uploaded_offer2 = st.file_uploader("Charger l’offre", type=["pdf", "docx", "txt"], key="offre2")
    if uploaded_cv2 and uploaded_offer2:
        cv_text2 = parser.extract_text(uploaded_cv2)
        offer_text2 = parser.extract_text(uploaded_offer2)
        letter = gpt_generation.generate_letter(cv_text2, offer_text2, offline=offline_mode)
        st.text_area("Lettre générée", letter, height=400)
        st.download_button("Télécharger la lettre", letter, file_name="lettre_motivation.txt")

# Onglet 3 : Alignement des compétences
with tabs[2]:
    st.header("Résumé & alignement des compétences")
    uploaded_cv3 = st.file_uploader("CV", type=["pdf", "docx"], key="cv3")
    uploaded_offer3 = st.file_uploader("Offre", type=["pdf", "docx", "txt"], key="offre3")
    if uploaded_cv3 and uploaded_offer3:
        cv_text3 = parser.extract_text(uploaded_cv3)
        offer_text3 = parser.extract_text(uploaded_offer3)
        summary = match_skills.compare_skills(cv_text3, offer_text3)
        st.write(summary)

# Onglet 4 : Optimisation wording
with tabs[3]:
    st.header("Optimisation du wording du CV")
    uploaded_cv4 = st.file_uploader("CV", type=["pdf", "docx"], key="cv4")
    uploaded_offer4 = st.file_uploader("Offre", type=["pdf", "docx", "txt"], key="offre4")
    if uploaded_cv4 and uploaded_offer4:
        cv_text4 = parser.extract_text(uploaded_cv4)
        offer_text4 = parser.extract_text(uploaded_offer4)
        suggestions = gpt_generation.optimize_wording(cv_text4, offer_text4, offline=offline_mode)
        st.write(suggestions)
