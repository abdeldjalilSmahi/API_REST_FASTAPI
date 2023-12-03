import requests
from server.baseModels.client_model import ClientModel
from server.baseModels.demade_model import DemandeModel
from server.baseModels.demade_model import ImmobilierModel

BASE_URL = "http://127.0.0.1:8000"  # Replace with the actual URL of your FastAPI server


class APIClient:
    def submit_demande(self, demande_data):
        client = demande_data["client"]
        immobilier = demande_data["demandes"]["immobilier"]
        montant = demande_data["demandes"]["montant"]
        duree = demande_data["demandes"]["duree"]
        client_model = ClientModel(id=client["id"], nom=client["nom"], prenom = client["prenom"], numero_tel =client["numero_tel"],
                                    email =client["email"], depense=client["depense"],revenu=client["revenu"] )
        immobilier_model = ImmobilierModel(num_appt=immobilier["num_appt"], num_rue= immobilier["num_rue"], rue = immobilier["rue"] ,code_postal=immobilier["code_postal"], ville = immobilier["ville"])
        demande_model = DemandeModel(client=client_model, immobilier=immobilier_model, montant=montant, duree=duree)
        url = f"{BASE_URL}/demandes"
        response = requests.post(url, json=demande_model.model_dump())
        return response.json()


def main():
    api_client = APIClient()
    print("Bonjour, bienvenue à l'espace de demande de prêt")

    # Informations du client
    id_client = int(input("Entrez votre identifiant : "))
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    numero_tel = input("Entrez votre numéro de téléphone : ")
    email = input("Entrez votre email : ")
    depense = float(input("Entrez votre dépense mensuelle : "))
    revenu = float(input("Entrez votre revenu mensuel : "))

    # Informations de la demande de prêt
    montant_demande = float(input("Entrez le montant du prêt souhaité : "))
    duree_demande = int(input("Entrez la durée du prêt en années : "))

    # Informations de l'immobilier
    num_appt = int(input("Entrez le numéro de l'appartement : "))
    num_rue = int(input("Entrez le numéro de la rue : "))
    rue = input("Entrez le nom de la rue : ")
    code_postal = int(input("Entrez le code postal : "))
    ville = input("Entrez la ville : ")

    # Affichage des informations recueillies
    print(f"Vous avez saisi les informations suivantes :")
    print(
        f"Client ID: {id_client}, Nom: {nom}, Prénom: {prenom}, Téléphone: {numero_tel}, Email: {email}, Dépense: {depense}, Revenu: {revenu}")
    print(
        f"Demande de prêt de {montant_demande}€ sur {duree_demande} ans pour l'immobilier situé au {num_appt}, {num_rue} {rue}, {code_postal} {ville}.")
    # Example of submitting a demande
    demande_data = {
        "client": {
            "id": id_client,
            "nom": nom,
            "prenom": prenom,
            "numero_tel": numero_tel,
            "email": email,
            "depense": depense,
            "revenu": revenu,
        },
        "demandes": {
            "montant": montant_demande,
            "duree": duree_demande,
            "immobilier": {
                "num_appt": num_appt,
                "num_rue": num_rue,
                "rue": rue,
                "code_postal": code_postal,
                "ville": ville
            }
        }
    }

    result = api_client.submit_demande(demande_data)
    print(result)


if __name__ == "__main__":
    main()
