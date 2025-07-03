CREATE TABLE IF NOT EXISTS eco_compteurs (
    id SERIAL PRIMARY KEY,
    compteur_id VARCHAR(50),
    nom_lieu VARCHAR(100),
    valeur INTEGER
);