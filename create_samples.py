import sys
import os
import pandas as pd
import glob

# Création des répertoires pour les échantillons
os.makedirs('data/sample/streamers', exist_ok=True)
os.makedirs('data/sample/events', exist_ok=True)
os.makedirs('data/sample/temporal', exist_ok=True)

# Fonction pour créer un échantillon
def create_sample(file_path, output_dir, n_rows=10):
    try:
        # Lire les n premières lignes du fichier CSV
        df = pd.read_csv(file_path, nrows=n_rows)
        
        # Créer le chemin de sortie
        filename = os.path.basename(file_path)
        output_path = os.path.join(output_dir, filename)
        
        # Sauvegarder l'échantillon
        df.to_csv(output_path, index=False)
        print(f"Échantillon créé : {output_path}")
    except Exception as e:
        print(f"Erreur lors de la création de l'échantillon pour {file_path}: {e}")

print("Création des échantillons pour les données ZEvent 2025...")

# Créer des échantillons pour les streamers
for csv_file in glob.glob('data/clean/streamers/*.csv'):
    create_sample(csv_file, 'data/sample/streamers')

# Créer des échantillons pour les événements
for csv_file in glob.glob('data/clean/events/*.csv'):
    create_sample(csv_file, 'data/sample/events')

# Créer des échantillons pour les données temporelles
for csv_file in glob.glob('data/clean/temporal/*.csv'):
    create_sample(csv_file, 'data/sample/temporal')

print("Tous les échantillons ont été créés avec succès !")