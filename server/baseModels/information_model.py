from pydantic import BaseModel
from .demade_model import DemandeModel

'''
    Modele de l'information
'''


class InformationPersonnelleClient(BaseModel):
    id_client: int
    nom: str
    prenom: str
    numero_tel: str
    email: str


class InformationFinanciereClient(BaseModel):
    id_client: int
    revenu: float
    depense: float
    montant_pret: float
    duree_pret: int


class InformationImmobilier(BaseModel):
    num_appt: int
    num_rue: int
    rue: str
    code_postal: int
    ville: str


class InformationModel(BaseModel):
    information_personnelle_client: InformationPersonnelleClient
    information_financiere_client: InformationFinanciereClient
    information_immobilier: InformationImmobilier

    # def __init__(self, demandeModel: DemandeModel, **data):
    #     super().__init__(**data)
    #     self.information_personnelle_client = InformationPersonnelleClient(demandeModel)
    #     self.information_financiere_client = InformationFinanciereClient(demandeModel)
