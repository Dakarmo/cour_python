from titanic_Game import TitanicStatistique

def main():
    # Créez une instance de TitanicStatistique en utilisant le chemin du fichier CSV
    titanic = TitanicStatistique('titanic.xls')

    while True:
        # Affichage du menu principal du gestionnaire de contacts
        print("*****MENU****")
        print(" 1: Afficher le contenu du fichier")
        print(' 2: Afficher la forme du DataFrame')  
        print(' 3: Afficher les entêtes du DataFrame')  
        print(' 4: Afficher le statistique descriptive de la colonne "Age"')
        print(' 5: Afficher le statistique descriptive de la colonne "Pclass"')
        print(' 6: Afficher les colonnes avec des données manquantes.')
        print(' 7: Afficher les lignes avec des données manquantes.')
        print(' 8: Afficher l\'histogramme des âges')
        print(' 9: Afficher l\'histogramme des classes')
        print('10: Afficher la moyenne des ages des survivants') 
        print('11: Afficher la moyenne des ages des non survivants') 
        print("0: Quitter")

        choix = input("Entrez votre choix (1-11) : ")

        if choix == '1':
            titanic.afficher_apercu()
        elif choix == '2':
            titanic.afficher_forme()
        elif choix == '3':
            titanic.afficher_entetes()
        elif choix == '4':
            titanic.afficher_statistiques_age()
        elif choix == '5':
            titanic.afficher_statistiques_pclass()
        elif choix == '6':
            titanic.afficher_colonnes_manquante()
        elif choix == '7':
            titanic.afficher_lignes_manquante()
        elif choix == '8':
            titanic.tracer_histogramme_ages()
        elif choix == '9':
            titanic.tracer_histogramme_classes()
        elif choix == '10':
            titanic.calculer_moyenne_age_survivants()
        elif choix == '11':
            titanic.calculer_moyenne_age_non_survivants()
        elif choix == '0':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 11.")

        # Demande à l'utilisateur s'il souhaite poursuivre
        # choice = input("Voulez-vous poursuivre ou quitter ? O/N : ")
        # print(choice.lower() )
        # if choice == "o" or choice == "oui" or choice == "O":
        #     main()
        # elif choice == "n" or choice == "non" or choice == "N":
        #     print("Au revoir !")
        #     break
        # else:
        #     print("Choix invalide.")

if __name__ == "__main__":
    main()
