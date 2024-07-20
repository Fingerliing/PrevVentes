import pandas as pd
import sqlite3

# Lire le fichier Excel
file_path = './data/ventes réelles 01avril2023 a 30decembre2023.xlsx'
df = pd.read_excel(file_path)
df.columns = df.columns.str.replace(' ', '_').str.replace("'", '').str.replace('/', '_').str.replace('(', '').str.replace(')', '')

print("Noms des colonnes après le remplacement :", df.columns)


# Connexion à la base de données SQLite (crée la base de données si elle n'existe pas)
conn = sqlite3.connect('ventes.db')
cursor = conn.cursor()

# Créer une table dans SQLite
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventes (
        Donneur_dordre TEXT,
        Article TEXT,
        Mois_Année_de_facturation TEXT,
        CA_Net REAL,
        Qté_facturée_Base_Unit REAL,
        Poids_Net REAL
    )
''')

# Insérer les données du DataFrame dans la table SQLite
df.to_sql('ventes', conn, if_exists='append', index=False)

# Valider les transactions et fermer la connexion
conn.commit()
conn.close()
