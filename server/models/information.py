from .demande import Demande

class Information:
    # demande: Demande
    information_personnelle_client: dict= {
        "id_client" : str,
        "nom" : str,
        "prenom" : str,
        "numero_tel" : str,
        "email" : str
    }
    information_finaniere_client: dict= {
        "revenu" : float,
        "depnse" : float,
        "montant_pret" : float,
        "duree_pret" : int
    }

    def __init__(self, demande):

        client = demande.client

        # Initialisez les dictionnaires ici
        self.information_personnelle_client = {}
        self.information_finaniere_client = {}

        # Remplissez les dictionnaires avec les informations nécessaires
        self.information_personnelle_client["id_client"] = client.id
        self.information_personnelle_client["nom"] = client.nom
        self.information_personnelle_client["prenom"] = client.prenom
        self.information_personnelle_client["numero_tel"] = client.numero_tel
        self.information_personnelle_client["email"] = client.email

        self.information_finaniere_client["revenu"] = client.revenu
        self.information_finaniere_client["depnse"] = client.depense
        self.information_finaniere_client["montant_pret"] = demande.montant
        self.information_finaniere_client["duree_pret"] = demande.duree
