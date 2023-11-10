from contact import Contact
from contact_manager import ContactManager


# Fonction principale du programme

def main():
    manager = ContactManager('bd.csv')

    while True:
        # Affichage du menu principale du gestionnaire de contacts
        print("Gestionnaire de Contacts")
        print("1. Ajouter un nouveau contact")
        print("2. Afficher tous les contacts")
        print("3. Mettre à jour un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        # L'utilisateur choisit une option
        choix = input("Choississez une option : ")

        if choix == "1":
            # Ajout d'un nouveau contact
            nom = input('Nom : ')
            prenom = input('Prenom : ')
            telephone = input('Téléphone : ')
            email = input('Email : ')

            if not manager.check_contact(email):
                contact = Contact(nom, prenom, telephone, email)
                manager.addContact(contact)
                print("Contact ajouté avec succès!")

        elif choix == "2":
            manager.showContacts()

        elif choix == "3":
            email = input("Email du contact à mettre à jour : ")

            if manager.check_contact(email):
                new_nom = input("Nouveau nom : ")
                new_prenom = input("Nouveau prenom : ")
                new_telephone = input("Nouveau téléphone : ")
                new_email = input("Nouveau email : ")

                new_contact = Contact(new_nom,
                                      new_prenom,
                                      new_telephone,
                                      new_email
                                      )

                manager.updateContact(email, new_contact)
                print("Contact mis à jour avec succès")
            else:
                 print("Aucun contact avec cet email n'a été trouvé.")
                 
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
             break
     


if __name__ == "__main__":
    main()
