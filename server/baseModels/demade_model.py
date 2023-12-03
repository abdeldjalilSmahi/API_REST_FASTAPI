from pydantic import BaseModel
from .client_model import ClientModel
from .immobilier_model import ImmobilierModel


class DemandeModel(BaseModel):
    client: ClientModel
    immobilier: ImmobilierModel
    montant: float
    duree: int
