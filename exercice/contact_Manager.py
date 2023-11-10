import csv

class ContactManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    def addContact(self, contact):
        # Ouvir le fichier csv en mode writting
        with open(self.csv_file, mode='a', newline='') as file:
            write = csv.writer(file) #Cré un objet writer qui pourra être appelé à chaque instant pour écrir dans le ficher csv
            # writer.writerow([1,2,3,4,5]) 
            #la ligne ci-dessous écrit une ligne dans le fichier csv avec  les information du contact
            write.writerow([contact.nom, contact.prenom, contact.telephone, contact.email]) 
        
    
    
    
    def showContacts(self):
        
        with open(self.csv_file, mode='r') as file:
            read = csv.reader(file)
            
            for row in read:
                # print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]},")
                print(("{}, {}, {}, {},").format(row[0], row[1], row[2], row[3]))
    
    
    def updateContact(self, email, newContact):
        with open(self.csv_file, mode='r', newline='') as file:
            read = csv.reader(file)
            rows = list(read) # Lit toutes les lignes du fichier et les stocke dans une liste.
            
        with open(self.csv_file, mode="w", newline='') as file:
            write = csv.writer(file)
            for row in rows:
                if row[3] == email:
                    write.writerow([newContact.nom, newContact.prenom, newContact.telephone, newContact.email])        
                else:
                    write.writerow(row)
        
        
    def deleteContact(self, email):
        with open(self.csv_file, mode='r', newline='') as file:
            read = csv.reader(file)
            rows = list(read) # Lit toutes les lignes du fichier et les stocke dans une liste.
        
        with open(self.csv_file, mode='w', newline='') as file:
            write = csv.writer(file)
            
            for row in rows:
                if row[3] != email:
                    # Si l'adresse email ne correspond pas à celle du contact à supprimer.
                    write.writerow(row)
                    # Reecrit les informations des contacts non supprimés.
                    
        
    
    def check_contact(self, email):
        #Cette fonction permet de vérifier si un contact existe
        
        # Ouvir le fichier csv en mode lecteur
        with open(self.csv_file, mode='r') as file:
            read = csv.reader(file) # Crée un objet reader pour lire le fichier csv.
            
            for row in read:
                if row[3] == email: #si l'adresse email correspond à celle d'un contact existant
                    return True
        
        return False #si le contact n'existe pas
        