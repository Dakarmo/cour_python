Est-ce que vous saviez que vous aviez plus de chances de survivre à bord du Titanic si vous étiez un homme qui voyageait en troisième classe plutôt qu'un homme qui voyageait en deuxième classe ?

Bref 🤦‍♂️🤦‍♀️. Moi même je ne sais pas.🤷‍♀️🤷‍♂️
On va le découvrir ensemble à travers cet exercice😊✔✨😁

Vous allez apprendre à vous servir de pandas, numpy et matplotlib pour analyser les données des passagers afin de prédire si quelqu'un survivrait au naufrage du Titanic ou pas s'il était un passager.

# Objectif : 
À travers cet exercice, vous serez amené(e) à utiliser les bibliothèques Python telles que Pandas, NumPy, Matplotlib et scikit-learn pour explorer et analyser un ensemble de données représentant les passagers du Titanic. Le but final est de créer un modèle de régression linéaire pour prédire la survie des passagers en fonction de certaines caractéristiques.

Étapes :

# 1- Importez les bibliothèques nécessaires (pandas, numpy, matplotlib).

# 2- Charger les fichier CSV "titanic.csv" dans un Dataframe Pandas.

# 3-Affichez la forme et les entêtes du DataFrame .

# 4- Effectuez une analyse statistique descriptive des colonnes age et pclass.

# 5- Identifier les lignes ou les colonnes avec des données manquantes.

# 6- Gérez les valeurs manquantes dans le DataFrame de manière appropriée .

# 7- Créez un histogramme des classes et des âges .

# 8- Calculez la moyenne de l'âge pour les survivants et les non-survivants .

# 9- Sélectionnez les caractéristiques pertinentes et divisez les données en données de tests et données d'entrainement.

# 10- Initialisez et entraînez un modèle de REGRESSION LINEAIRE.

# 11- Charger le model et Prédisez les valeurs pour l'ensemble de test et évaluez les performances.

# 12- Affichez un graphe pour visualiser l'ajustement du modèle en traçant les prédictions par rapport aux valeurs réelles.

# 13- Tu peux utiliser le modèle entraîné pour faire des prédictions sur de nouvelles données. Assure-toi simplement que ces nouvelles données ont les mêmes caractéristiques que celles sur lesquelles le modèle a été entraîné (c'est-à-dire 'pclass', 'age').

# 14- Tu peux utiliser une simple condition pour transformer la prédiction continue en une prédiction binaire (0 pour non survécu, 1 pour survécu). Voici comment tu pourrais le faire


## Définition 

La régression linéaire est un modèle statistique qui cherche à établir une relation linéaire entre une variable dépendante (cible) et une ou plusieurs variables indépendantes (caractéristiques). Elle est souvent utilisée dans des tâches de prédiction où l'objectif est de faire des prédictions basées sur des données existantes.

La forme générale d'une régression linéaire simple (avec une seule caractéristique) est représentée par l'équation :

Y = aX + b + e

Y : est la variable dépendante (cible),
X : est la variable indépendante (caractéristique),
b : est l'ordonnée à l'origine (intercept),
a : est la pente (coefficient de régression),
e  : est le terme d'erreur.

L'objectif de la régression linéaire est de trouver les valeurs des coefficients (a) qui minimisent la somme des carrés des erreurs (e²) entre les valeurs prédites et les valeurs réelles. Cela est souvent réalisé en utilisant la méthode des moindres carrés.

Dans une régression linéaire multiple (avec plusieurs caractéristiques), l'équation s'étend pour inclure toutes les caractéristiques et leurs coefficients associés.

Les régressions linéaires sont largement utilisées dans la modélisation prédictive et l'analyse statistique, et elles constituent la base de nombreuses techniques plus avancées. Elles sont relativement simples à interpréter, mais elles supposent une relation linéaire entre les variables, ce qui peut ne pas être approprié dans tous les cas.