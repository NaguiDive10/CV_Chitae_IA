# utils/gpt_generation.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Charger les variables d’environnement
load_dotenv()

# Initialiser le client avec la clé API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_gpt(prompt, role="Tu es un assistant RH professionnel.", model="gpt-3.5-turbo", max_tokens=1000, offline=False):
    """
    Appelle l'API OpenAI (ou simule une réponse en mode hors ligne).
    """
    if offline:
        return (
            "[MODE HORS LIGNE ACTIVÉ]\n"
            f"---\nPrompt reçu :\n{prompt[:500]}...\n---\n"
            "(Sortie fictive générée pour test hors ligne)"
        )

    try:
        if not client.api_key:
            raise ValueError("Clé API OpenAI manquante. Vérifiez votre fichier .env")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )

        if not response.choices:
            return "⚠️ Aucune réponse générée par le modèle."

        return response.choices[0].message.content.strip()

    except Exception as e:
        if "quota" in str(e).lower():
            return (
                "❌ Erreur : quota OpenAI dépassé.\n"
                "💡 Vérifiez votre plan ici : https://platform.openai.com/account/usage"
            )
        return f"❌ Erreur lors de l'appel à GPT : {e}"

def generate_adapted_cv(cv_text, job_offer_text, offline=False):
    prompt = f"""
Tu es un expert RH. Voici un CV original :

{cv_text}

Et voici une offre d’emploi :

{job_offer_text}

Génère un nouveau CV structuré, adapté à cette offre, mettant en valeur les expériences pertinentes et en reprenant les mots-clés de l'offre. Réécris uniquement les parties utiles et supprime le superflu. Sois professionnel, synthétique et clair.
"""
    return call_gpt(prompt, role="Tu es un assistant RH expert en rédaction de CV.", offline=offline)

def generate_letter(cv_text, job_offer_text, offline=False):
    prompt = f"""
Tu es un assistant RH. Génère une lettre de motivation professionnelle pour cette offre :

{job_offer_text}

Basée sur ce CV :

{cv_text}

Commence par une introduction personnalisée, puis valorise les expériences pertinentes, et termine par une ouverture pour un entretien.
"""
    return call_gpt(prompt, role="Tu es un assistant RH spécialisé en lettres de motivation.", offline=offline)

def optimize_wording(cv_text, job_offer_text, offline=False):
    prompt = f"""
Voici un CV :

{cv_text}

Et une offre d’emploi :

{job_offer_text}

Propose des reformulations précises du CV pour qu’il contienne plus de mots-clés pertinents par rapport à l'offre. Donne la liste des phrases optimisées, et sur quelles lignes/sections du CV les appliquer.
"""
    return call_gpt(prompt, role="Tu es un expert RH en wording et optimisation ATS.", offline=offline)
