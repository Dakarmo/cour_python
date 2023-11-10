import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TitanicStatistique:
    def __init__(self, chemin_fichier_csv):
        self.df = pd.read_excel(chemin_fichier_csv)

    def afficher_statistiques_age(self):
        description_age = self.df['Age'].describe()
        print("Statistiques descriptives pour la colonne 'Age':")
        print(description_age)

    def afficher_statistiques_pclass(self):
        description_pclass = self.df['Pclass'].describe()
        print("\nStatistiques descriptives pour la colonne 'Pclass':")
        print(description_pclass)

    def afficher_forme(self):
        forme = self.df.shape
        print("\nForme du DataFrame : ", forme)

    def afficher_entetes(self):
        entetes = self.df.columns
        print("\nEntêtes du DataFrame : ", entetes)
        
    def afficher_colonnes_manquante(self):
        colonneManquantes = self.df.columns[self.df.isnull().any()].tolist()
        print("\nColonnes avec des données manquantes :", colonneManquantes)
        
    def afficher_lignes_manquante(self):
        ligneManquantes = self.df[self.df.isnull().any(axis=1)]
        print("\nLignes avec des données manquantes :\n", ligneManquantes)
        
    def tracer_histogramme_classes(self):
        plt.figure(figsize=(8, 6))
        self.df['Pclass'].hist(bins=3, edgecolor='black', alpha=0.7)
        plt.title('Histogramme des Classes')
        plt.xlabel('Classe')
        plt.ylabel('Nombre de passagers')
        plt.show()

    def tracer_histogramme_ages(self):
        plt.figure(figsize=(10, 6))
        self.df['Age'].hist(bins=20, edgecolor='black', alpha=0.7)
        plt.title('Histogramme des Âges')
        plt.xlabel('Âge')
        plt.ylabel('Nombre de passagers')
        plt.show()
        
    def calculer_moyenne_age_survivants(self):
        moyenne_age_survivants = self.df[self.df['Survived'] == 1]['Age'].mean()
        print(f"Moyenne d'âge pour les survivants : {moyenne_age_survivants:.2f} ans")

    def calculer_moyenne_age_non_survivants(self):
        moyenne_age_non_survivants = self.df[self.df['Survived'] == 0]['Age'].mean()
        print(f"Moyenne d'âge pour les non-survivants : {moyenne_age_non_survivants:.2f} ans")

    def afficher_apercu(self):
        apercu = self.df.head()
        print("\nAperçu du DataFrame :")
        print(apercu)
        
    