from pydantic import BaseModel

class ClientModel(BaseModel):
    id: int
    nom: str
    prenom: str
    numero_tel: str
    email: str
    depense: float
    revenu: float
