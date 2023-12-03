
from fastapi import FastAPI

import os
import json
import requests
from server.baseModels.information_model import InformationModel, InformationPersonnelleClient, InformationFinanciereClient, InformationImmobilier
from server.baseModels.client_model import ClientModel
from server.baseModels.demade_model import DemandeModel
from server.baseModels.immobilier_model import ImmobilierModel

## 127.0.0.1:8001


app = FastAPI()



# Obtenez le chemin absolu du répertoire 'server'
server_dir = os.path.dirname(os.path.abspath(__file__))

# Changez le répertoire de travail vers le répertoire 'server'
os.chdir(server_dir)

# Maintenant vous pouvez utiliser des chemins relatifs par rapport à 'server'


def lancement_service_approbation(information, url_service="http://127.0.0.1:8080/approbation"):
    print("extraction.py : declanchement de la fonction : lancement_service_approbation")
    # Utilisez requests pour envoyer une requête POST au service d'approbation
    response = requests.post(url_service, json=information.dict())

    # Vérifiez la réponse si nécessaire
    if response.status_code == 200:
        print("Service d'approbation déclenché avec succès.")
        # information_dict = response.json()
        print("Contenu du dictionnaire 'information' retourné par le service d'approbation :")
        # print(information_dict)
        # return response
    else:
        print(f"Erreur lors du déclenchement du service d'approbation : {response.status_code}")


## 127.0.0.1:8001

@app.post("/extract/informations/{file_name}")
def extract(file_name):
    path = f"demandes/{file_name}.json"
    with open(path, 'r') as file:
        data = json.load(file)

    client_data = data.get("client", {})
    # print("Extracted client_data:", client_data)
    #
    derniere_demande = data.get("demandes", [])[-1]
    montant = derniere_demande.get("montant")
    duree = derniere_demande.get("duree")
    immobilier = derniere_demande.get("immobilier", {})
    #
    # client
    id = client_data.get("id")
    nom = client_data.get("nom")
    prenom = client_data.get("prenom")
    numero_tel = client_data.get("numero_tel")
    email = client_data.get("email")
    depense = client_data.get("depense")
    revenu = client_data.get("revenu")

    #immobilier
    num_appt = immobilier["num_appt"]
    num_rue = immobilier["num_rue"]
    rue = immobilier["rue"]
    code_postal = immobilier["code_postal"]
    ville = immobilier["ville"]


    client_model = ClientModel(id=id, nom=nom, prenom=prenom, numero_tel=numero_tel, email=email, depense=depense,
                               revenu=revenu)

    immobilier_model = ImmobilierModel(num_appt=num_appt, num_rue=num_rue, rue=rue, code_postal=code_postal, ville=ville)

    demande_model = DemandeModel(client=client_model, immobilier=immobilier_model, montant=montant, duree=duree)

    information_personnelle = InformationPersonnelleClient(id_client=id, nom=nom, prenom=prenom, numero_tel=numero_tel,
    email=email)

    information_financiere = InformationFinanciereClient(id_client=id, revenu=revenu, depense=depense, montant_pret=montant,
    duree_pret=duree)

    information_immobilier = InformationImmobilier(num_appt=num_appt, num_rue=num_rue, rue=rue, code_postal=code_postal, ville=ville)

    information_model = InformationModel(
        information_personnelle_client=information_personnelle,
        information_financiere_client=information_financiere,
        information_immobilier=information_immobilier
    )
    print("extractnion.py : juste avant le declanchement de service composite")
    lancement_service_approbation(information_model)




