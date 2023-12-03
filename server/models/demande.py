from .client import Client
from .immobilier import Immobilier

class Demande():
    client : Client
    immobilier : Immobilier
    montant : float
    duree : int

    def __init__(self, client, immobilier ,montant, duree):
        self.client = client
        self.immobilier = immobilier
        self.montant = montant
        self.duree = duree

    def to_dict(self):
        return {
            "client": self.client.to_dict(),
            "immobilier_demande": self.immobilier.to_dict(),
            "montant": self.montant,
            "duree": self.duree
        }




