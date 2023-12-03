from pydantic import BaseModel

class ElementDicisionModel(BaseModel):
    score_fico : float
    score_propriete : float
    montant_demande : float
    prix : float