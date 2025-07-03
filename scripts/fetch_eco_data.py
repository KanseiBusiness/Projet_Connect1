import requests, psycopg2
from config import DB_CONFIG
def run():
    print("Collecte eco_compteurs...")
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    url = "https://portail-api.montpellier3m.fr/eco_compteurs.json"
    data = requests.get(url).json()
    for row in data:
        cur.execute("INSERT INTO eco_compteurs (compteur_id, nom_lieu, valeur) VALUES (%s, %s, %s)",
                    (row.get("id"), row.get("nom"), row.get("valeur", 0)))
    conn.commit()
    cur.close()
    conn.close()
