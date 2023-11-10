import csv

class ContactManager:
     def __init__(self, csv_file):
          self.csv_file = csv_file
          
     def addContact(self, contact):
          with open(self.csv_file, mode='a', newline='') as file:
               #Ouvrir le fichier en mode ajout ('a')
               writer = csv.writer(file) #Crée un objet  writer pour ecrire dans le fichier csv
               # writer.writerow([1,2,3,4,5,6])
               writer.writerow([contact.nom, contact.prenom, contact.telephone, contact.email])
               # Ecrire une nouvelle ligne dans le fichier csv avec les informations du contact.
               
     def showContacts(self):
          #Cette methode permet d'afficher tous les constacts du fichier csv
          with open(self.csv_file, mode='r') as file:
               reader = csv.reader(file)
               
               for row in reader:
                    
                    print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}")
                    print(("{}, {}, {}, {}").format(row[0],row[1],row[2],row[3]))
                    
     def updateContact(self, email, new_contact):
          with open(self.csv_file, mode='r', newline='') as file:
               reader = csv.reader(file)
               rows = list(reader) # Lit toutes les lignes du fichier et les stocke dans une liste.
               
          with open(self.csv_file, mode='w', newline='') as file:
               writer = csv.writer(file)
               for row in rows:
                    if row[3] == email:
                         writer.writerow([new_contact.nom, new_contact.prenom, new_contact.telephone, new_contact.email])
                         #Ecrit les nouvelles informations du contact
                    else:
                         writer.writerow(row)
                         #Ecrit les informations inchangées des autres contacts.
               
     def deleteContact(self, email):
          with open(self.csv_file, mode='r', newline='') as file:
               reader = csv.reader(file)
               rows = list(reader) # Lit toutes les lignes du fichier et les stocke dans une liste.
               
          with open(self.csv_file, mode='w', newline='') as file:
               writer = csv.writer(file)
               
               for row in rows:
                    if row[3] != email:
                    # Si l'adresse email ne correspond pas à celle du contact à supprimer.
                         writer.writerow(row)
                         # Reecrit les informations des contacts non supprimés.
                    
          
               
     def check_contact(self, email):
          # Cette fonction permet de vérifier si un contact existe dans le fichier csv par son adress email.
          
          with open(self.csv_file, mode='r') as file:
               #Ouvrir le fichier csv en model lecture ('r')
               reader = csv.reader(file) # Crée un objet reader pour lire le fichier CSV.
               
               for row in reader:
                    if row[3] == email:
                         # Si l'adresse email correspond à celle d'un contact existant.
                         return True # Pour indiquer que le contact existe
                    
          return False # Retourne False si le contact n'existe pas.
                         
          