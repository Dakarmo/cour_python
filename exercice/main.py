from contact import Contact
from contact_Manager import ContactManager

#fonction principale du programme

def main():
    manager = ContactManager('bd.csv')
    while True:
        #Affichage du menu principale du gestionnaire de contacts
        print("Gestionnaire de Contacts")
        print("1: Ajouter un nouveau contact")
        print("2: Afficher tous les contacts")
        print("3: Mettre à jour un contact")
        print("4: Supprimer un contact")
        print("5: Quitter")
        
        #L'utilisateur choisit une option
        choix = input("Choississez une option ")
        
        if choix == "1":
            #Ajout d'un nouveau contact
            nom = input("Veuillez entrer votre Nom : ")
            prenom = input("Veuillez entrer votre Prenom : ")
            telephone = input("Veuillez entrer votre Téléphone : ")
            email = input("Veuillez entrer votre Email : ")
            
            if not manager.check_contact(email):
                contact = Contact(nom, prenom, telephone, email)
                manager.addContact(contact)
                print("Bravo, Contact enrégistré avec succès !")
                choice = input("Voulez vous ajouter un nouveau contact ? oui/non : ")
                if choice =="oui" or choice == 'o':
                    choix = "1"
                elif choice == "non" or choice == "n":
                    main()
                
        elif choix == "2":
            # print('hello')
            manager.showContacts()
        
        elif choix =="3":
            email = input('Email du contatct à mettre à jour : ')
            
            if manager.check_contact(email):
                new_nom = input("Veuillez entrer le nouveau Nom : ")
                new_prenom = input("Veuillez entrer le nouveau Prenom : ")
                new_telephone = input("Veuillez entrer le nouveau Téléphone : ")
                new_email = input("Veuillez entrer le nouveau Email : ")

                new_contact = Contact(new_nom, new_prenom, new_telephone, new_email)
                
                new_contact = manager.updateContact(email, new_contact)
                print("Bravo, Contact mise à jour avec succès !")
                manager.showContacts()
            else:
                print("Aucun contact n'est trouvé avec ce email")

        elif choix == "4":
            # Suppression d'un contact par son email
            email = input("Email du contact à supprimer : ")
             
            if manager.check_contact(email):
                manager.deleteContact(email)
                print("Contact supprimé avec succès")
            else:
                print("Aucun contact avec cet email n'a été trouvé")
                  
        elif choix == "5":
            # Sortir du programme si l'utilisateur décide de quitter le programme.
            print("Au revoir !")
            break
        else:
            print("Choix incorrect")
            print("Veuillez bien lire et suivre les instructions.")
            
            
if __name__ == "__main__":
    main()