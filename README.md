# Adaptateur de CV IA

Ce projet Streamlit permet d'adapter automatiquement un CV et de générer une lettre de motivation à partir d’une offre d’emploi grâce à l’IA (OpenAI). Il fournit également un résumé des compétences et des optimisations de wording.

## Fonctionnalités

L'application se compose de **4 onglets** interactifs :

1. **Générer un CV adapté** : transforme le CV selon l'offre.
2. **Lettre de motivation** : rédige automatiquement une lettre.
3. **Résumé & alignement des compétences** : extrait les compétences clés du CV et les compare à celles de l'offre.
4. **Optimisation du wording** : propose des reformulations optimisées pour les ATS (systèmes de tri automatique).

## Architecture du projet

rh_dashboard_ia/
│
├── data/ # Données utilisateur (CV, offres)
├── models/ # (optionnel) modèles IA si apprentissage
├── notebooks/ # Explorations et prototypage
│
├── app.py # Interface principale Streamlit
├── train_models.py # Script d'entraînement de modèles (optionnel)
├── rh_analysis.py # Traitements et analyses RH
│
├── utils/
│ ├── parser.py # Extraction de texte (PDF, DOCX, TXT)
│ ├── gpt_generation.py # Fonctions OpenAI (avec mode offline)
│ └── match_skills.py # Comparaison de compétences
│
├── requirements.txt # Dépendances Python
├── .gitignore # Fichiers à exclure de Git
└── README.md # Documentation du projet

bash


## Prérequis

- Python 3.9+
- Compte OpenAI (clé API si mode en ligne)

## Installation

```bash
git clone https://github.com/votre-utilisateur/rh_dashboard_ia.git
cd rh_dashboard_ia
python -m venv venv
source venv/bin/activate     # sous Windows : venv\Scripts\activate
pip install -r requirements.txt
Configuration
Créer un fichier .env à la racine avec :

ini
Copier
Modifier
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
⚠️ Si vous ne disposez pas d’une clé API, activez le mode offline pour tester localement.

Lancement
bash
Copier
Modifier
streamlit run app.py
L’interface s’ouvre dans le navigateur. Vous pouvez charger vos fichiers et interagir avec les différentes options.

Mode hors ligne (offline)
En cas de quota dépassé ou sans clé API, vous pouvez activer le mode hors ligne dans app.py ou gpt_generation.py :

python

generated_cv = gpt_generation.generate_adapted_cv(cv_text, offer_text, offline=True)
Cela simule une réponse IA pour continuer vos tests sans requêtes externes.

Exemple d’utilisation
Charger un CV au format .pdf ou .docx

Charger une offre d’emploi (même format ou .txt)

Obtenir une version adaptée du CV ou une lettre directement téléchargeable

Contributions
Les contributions sont les bienvenues via pull request. Merci de documenter les modifications.

Licence
Ce projet est open source sous licence MIT.