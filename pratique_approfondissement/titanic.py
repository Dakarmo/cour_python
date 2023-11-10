import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

chemin_vers_titanic_csv = "titanic.csv"

# Chargez le fichier CSV dans un DataFrame Pandas
titanic_df = pd.read_csv(chemin_vers_titanic_csv)
# titanic_df = pd.read_csv(chemin_vers_titanic_csv, delimiter=',', dtype={'Age': float, 'Survived': str})

# Affichez les premières lignes du DataFrame pour vérifier si le chargement a réussi
print(titanic_df.head())

# Analyse statistique descriptive pour la colonne "Age"
description_age = titanic_df['Age'].describe()
print("Statistiques descriptives pour la colonne 'Age':")
print(description_age)

# Analyse statistique descriptive pour la colonne "Pclass"
description_pclass = titanic_df['Pclass'].describe()
print("\nStatistiques descriptives pour la colonne 'Pclass':")
print(description_pclass)


    