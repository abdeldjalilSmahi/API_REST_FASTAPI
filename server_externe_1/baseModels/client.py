from pydantic import BaseModel


class HistoryModel(BaseModel):
    revenu: float
    depense: float
    montant: float
    duree: int
    dettes: float
    anterieurs_de_paiement: float


class ClientModelFinance(BaseModel):
    id: int
    history: HistoryModel
