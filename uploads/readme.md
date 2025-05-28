📘 Cahier des Charges – IA Adaptateur de CV
🎯 Objectif général :
Créer une application web (Streamlit) permettant à un utilisateur de charger son CV et une offre d’emploi, puis d’utiliser l’IA pour :

Générer un nouveau CV adapté à l’offre (DOCX/PDF)

Générer une lettre de motivation adaptée

Comparer/Aligner les compétences du CV et de l’offre

Optimiser le wording du CV pour passer les filtres ATS

👤 Utilisateur cible :
Tout candidat en recherche de stage, alternance ou emploi, souhaitant personnaliser rapidement ses candidatures.

🧩 Fonctionnalités détaillées par onglet :
Onglet 1 – Générateur de CV adapté
Chargement CV original (DOCX, PDF)

Chargement offre (texte, DOCX, PDF)

Génération d’un nouveau CV (format texte ou DOCX/PDF)

Téléchargement direct

Onglet 2 – Lettre de motivation
Extraction automatique d’éléments du CV et de l’offre

Prompting GPT personnalisé

Téléchargement de la lettre (PDF ou texte)

Onglet 3 – Résumé et alignement des compétences
Extraction des compétences du CV

Extraction des compétences attendues dans l’offre

Affichage comparatif (barre de progression, tableau, etc.)

Onglet 4 – Optimisation du wording
Analyse des mots-clés de l’offre

Analyse du CV (sémantique + NLP)

Suggestions de reformulations ou insertions de mots clés

🏗️ Architecture du Projet
java
Copier
Modifier
cv_optimizer_app/
│
├── app.py                      ← Entrée principale Streamlit (avec tabs)
├── utils/
│   ├── parser.py               ← Extraction texte depuis PDF/DOCX
│   ├── match_skills.py         ← Alignement sémantique des compétences
│   ├── gpt_generation.py       ← Appels GPT pour génération intelligente
│   ├── cv_builder.py           ← Génération DOCX final
│
├── templates/                  ← Prompts & templates LM/CV
│   └── prompt_cv.txt
│   └── prompt_lm.txt
│
├── uploads/                    ← Fichiers chargés temporairement
├── requirements.txt
└── README.md

Exécute cette commande :
pip install -r requirements.txt

📦 Dépendances (requirements.txt)
txt
Copier
Modifier
streamlit
python-docx
PyMuPDF
pdfplumber
pandas
scikit-learn
openai
sentence-transformers
unidecode
python-dotenv

💡 Bonus (recommandé) : environnement virtuel
Pour isoler ton projet :

bash

python -m venv venv
venv\Scripts\activate   # sous Windows
# ou
source venv/bin/activate  # sous Linux/macOS

pip install -r requirements.txt


🔐 Étapes pour obtenir ta clé API :
1. Connecte-toi à https://platform.openai.com
(Utilise le même compte que pour ChatGPT)

2. Va dans le menu "API Keys"
Ou directement ici : https://platform.openai.com/account/api-keys

3. Clique sur "Create new secret key"
Donne un nom si tu veux

Tu obtiendras une clé commençant par sk-...

4. Copie-la immédiatement
Tu ne pourras plus la revoir plus tard !

Stocke-la dans ton .env ou dans un gestionnaire de secrets

⚠️ Ne partage jamais ta clé
Elle donne un accès payant à ton compte OpenAI

Si tu veux la stocker dans un dépôt GitHub, utilise un fichier .env non versionné grâce à .gitignore

