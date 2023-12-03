import smtplib
from email.mime.text import MIMEText

from fastapi import FastAPI, Body
import json
import requests
import os

from server.baseModels.information_model import InformationModel
from server.baseModels.decisionElementModel import ElementDicisionModel
from server_externe_1.baseModels.client import ClientModelFinance, HistoryModel
from server_externe_2.baseModels.immobilier_model import ImmobilierModelProp

app = FastAPI()

###  http://127.0.0.1:8080
# Service historique_client

# Obtenez le chemin absolu du répertoire 'server'
server_dir = os.path.dirname(os.path.abspath(__file__))

# Changez le répertoire de travail vers le répertoire 'server'
os.chdir(server_dir)


# Maintenant vous pouvez utiliser des chemins relatifs par rapport à 'server'

@app.get("/historique_clients/{client_id}")
async def recuperation_historique_client(client_id):
    with open(f"historique_clients/{client_id}.json", 'r') as file:
        historique_client = json.load(file)

    return {"historique": historique_client["historique"]}


@app.post("/decision")
async def prendre_decision(elemnts_decision: ElementDicisionModel = Body()):
    element_decision = elemnts_decision.dict()
    score_fico_valeur = element_decision["score_fico"]
    score_propriete_valeur = element_decision["score_propriete"]
    montant_demande = element_decision["montant_demande"]
    prix = element_decision["prix"]
    return {
        "decision": decision(score_fico_valeur, score_propriete_valeur, montant_demande, prix)
    }


def decision(score_fico, score_properite, montant_demande, prix_appart):
    if (montant_demande / prix_appart) > 1.2:
        return "Refusé Prix Demandé Trop Eleve"
    elif (prix_appart / montant_demande) > 1.2:
        return "Pret que vous avez demande est insuffisant"
    else:
        # Poids des scores
        fico_weight = 0.6
        property_weight = 0.4

        # Calcul des scores pondérés
        weighted_fico_score = score_fico * fico_weight
        weighted_property_score = score_properite * property_weight

        # Score combiné
        combined_score = weighted_fico_score + weighted_property_score

        # Seuil de décision
        decision_threshold = 0.6  # Par exemple, un seuil de 0,7

        # Décision
        if combined_score >= decision_threshold:
            return "Votre demande du pret a ete Approuvé"
        else:
            return "Votre demande du pret a ete Refusé"


def calcul_fico_with_service(client_id, revenu, depense, montant, duree, dettes, anterieurs_de_paiement):
    history = HistoryModel(revenu=revenu,
                           depense=depense,
                           montant=montant,
                           duree=duree,
                           dettes=dettes,
                           anterieurs_de_paiement=anterieurs_de_paiement)
    client_model_finance = ClientModelFinance(id=client_id, history=history)
    # Convertissez l'instance de ClientModelFinance en JSON pour l'envoyer avec la requête POST
    response_fico = requests.post(
        "http://127.0.0.1:8081/calcul-fico",
        json=client_model_finance.dict()
    )
    # Retournez la réponse JSON de l'API
    return response_fico.json()


def calcul_score_property(num_appt: int, num_rue: int, rue: str, code_postal: int, ville: str):
    print("welcome to la fonction de calcul score property")
    immobilier = ImmobilierModelProp(num_appt=num_appt, num_rue=num_rue, rue=rue, code_postal=code_postal,
                                     ville=ville)
    print("j'ai transmis au ImmobilierModelProp")

    reponse_prop = requests.post(
        "http://127.0.0.1:8082/calcul-score-pro",
        json=immobilier.dict()
    )
    print("j'ai recu une réponse de score property")
    return reponse_prop.json()

def Send_Mail(decision, mail):
    msg = MIMEText(decision)
    msg['Subject'] = "Retour de votre demande du pret"
    msg['From'] = "clc98025@gmail.com"
    msg['To'] = mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login("clc98025@gmail.com", "wthn tpba lcyj dput")
        smtp_server.sendmail("clc98025@gmail.com", mail, msg.as_string())
    print("Message sent!")


# Service approbation_demande
@app.post("/approbation")
def approbation_demande(informationModel: InformationModel = Body()):
    print("Je suis le service composite d'approbation ")
    information = informationModel.model_dump()
    print("j'ai recuppéré les infoos ")
    client_id = information["information_personnelle_client"]["id_client"]
    information_personnelle = information["information_personnelle_client"]
    email = information_personnelle["email"]
    information_financiere = information["information_financiere_client"]
    information_immobilier = information["information_immobilier"]
    print("j'ai recuppéré les infoos  perso, financ, immobilier")
    # informations finanicière
    revenu = information_financiere["revenu"]
    depense = information_financiere["depense"]
    montant = information_financiere["montant_pret"]
    duree = information_financiere["duree_pret"]
    print("j'ai recuppéré les details financière ")
    # Faire une requête au service historique_client pour récupérer l'historique
    ## phase 1 : réccupération de l'historique de client
    print("recup l'historique client")
    response_history = requests.get(f"http://127.0.0.1:8080/historique_clients/{client_id}")
    historique_client = response_history.json()
    historique_client = historique_client["historique"][-1]
    dette = historique_client["dettes"]
    anterieures_de_paiement = historique_client["anterieurs_de_paiement"]
    print("j'ai reussi a recupperer l'historique client ")
    ## phase 2: réccupération de scpre fico
    fico = calcul_fico_with_service(client_id, revenu, depense, montant, duree, dette, anterieures_de_paiement)
    score_fico = fico["score_fico"]
    print("j'ai caluclé le score fico ")
    ## phase 3: verification de la conformite immobilier
    print("phase immobilier  commence ")
    num_appt = information_immobilier["num_appt"]
    num_rue = information_immobilier["num_rue"]
    rue = information_immobilier["rue"]
    code_postal = information_immobilier["code_postal"]
    ville = information_immobilier["ville"]
    print("j'ai récupéré les informations immobilier et je vais les envoyer maintenant")
    immobilier_score = calcul_score_property(num_appt, num_rue, rue, code_postal, ville)
    ###Phase 4 : Calcul de decision
    print("la dernière phase : prise de decision")
    score_propriete = immobilier_score["property_score"]
    prix = immobilier_score["prix"]
    decisionelementModel = ElementDicisionModel(score_fico=score_fico, score_propriete=score_propriete,
                                                montant_demande=montant, prix=prix)
    print("je vais rentrer dans le service de prise de decision")
    decision = requests.post(f"http://127.0.0.1:8080/decision", json=decisionelementModel.model_dump())
    decision_finale = decision.json()
    Send_Mail(decision_finale["decision"], email)
    return decision_finale

