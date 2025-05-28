# utils/match_skills.py

from sentence_transformers import SentenceTransformer, util
import re

# Chargement du modèle de similarité
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_keywords(text):
    # Très simple extraction de compétences potentielles
    # Tu peux le remplacer par un vrai extracteur ou une liste de compétences
    words = re.findall(r'\b\w{3,}\b', text.lower())
    stopwords = {"avec", "dans", "pour", "les", "une", "des", "par", "sur", "ses", "son", "donc", "vous", "avoir"}
    return list(set([word for word in words if word not in stopwords]))

def compare_skills(cv_text, job_offer_text):
    cv_keywords = extract_keywords(cv_text)
    job_keywords = extract_keywords(job_offer_text)

    if not cv_keywords or not job_keywords:
        return "Pas assez d'informations pour extraire les compétences."

    # Embeddings
    cv_embeddings = model.encode(cv_keywords, convert_to_tensor=True)
    job_embeddings = model.encode(job_keywords, convert_to_tensor=True)

    # Similarité croisée
    results = []
    for i, job_kw in enumerate(job_keywords):
        similarities = util.cos_sim(job_embeddings[i], cv_embeddings)[0]
        max_score = float(similarities.max())
        best_match = cv_keywords[similarities.argmax()]
        results.append((job_kw, best_match, round(max_score, 2)))

    # Formatage
    table = "| Compétence de l'offre | Compétence dans le CV | Similarité |\n"
    table += "|------------------------|------------------------|------------|\n"
    for job_kw, match_kw, score in sorted(results, key=lambda x: -x[2]):
        table += f"| {job_kw} | {match_kw} | {score} |\n"

    return table
