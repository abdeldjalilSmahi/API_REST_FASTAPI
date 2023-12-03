import json
import os

class Persistor:
    def __init__(self, id_client, directory="demandes/"):
        self.id_client = id_client
        self.directory = directory
        self.file_path = os.path.join(self.directory, f"{self.id_client}.json")
        print(self.file_path)

    def save_demande(self, demande):
        # Vérifier si le fichier existe déjà
        if os.path.exists(self.file_path):
            # Lire le contenu existant
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            # Supprimer le fichier existant
            os.remove(self.file_path)
        else:
            # Créer une nouvelle structure de données pour le client
            data = {
                "client": demande.client,
                "demandes": []
            }
        # Ajouter la nouvelle demande à la liste des demandes
        data['demandes'].append({
            'montant': demande.montant,
            'duree': demande.duree,
            'immobilier': demande.immobilier
        })
        # Écrire les données mises à jour dans le fichier
        with open(self.file_path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def read_demandes(self):
        # Lire le contenu du fichier s'il existe
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        else:
            return None