from fastapi import FastAPI, Body
from baseModels.client import ClientModelFinance

app = FastAPI()

###   http://127.0.0.1:8081


@app.post("/calcul-fico")
async def calcul_score_fico(client: ClientModelFinance = Body()):
    # Pas besoin de 'model_dump', accédez directement aux attributs
    client_hist = client.dict()
    history = client_hist["history"]
    revenu = history["revenu"]
    depense = history["depense"]
    montant = history["montant"]
    duree = history["duree"]
    dettes = history["dettes"]
    anterieurs_de_paiement = history["anterieurs_de_paiement"]
    # Supposons que 'calculer_score_fico' est une fonction définie ailleurs
    score_fico = calculer_score_fico(revenu, depense, duree, dettes, anterieurs_de_paiement)
    return {"score_fico": score_fico}


def calculer_score_fico(revenus, depenses, duree, dettes, anterieurs_de_paiement):
    revenu_net = revenus - depenses
    ratio_dettes_revenu = dettes / revenu_net if revenu_net > 0 else 0
    score_paiement = 1 - anterieurs_de_paiement / 100
    # Calculer le score de durée du client.
    score_duree = 1 - duree / 100
    # Combiner les facteurs pour calculer le score FICO.
    score_fico = 0.6 * (1 - ratio_dettes_revenu) + 0.2 * \
                 score_paiement + 0.2 * score_duree
    # Limiter le score FICO dans la plage de 0.3 à 0.85
    score_fico = max(0.3, min(0.85, score_fico))
    return score_fico
    # pass