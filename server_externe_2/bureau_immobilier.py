import os
import json
from fastapi import FastAPI, Body
from baseModels.immobilier_model import ImmobilierModelProp

app = FastAPI()



###   http://127.0.0.1:8082
def find_propriete(num_appt, num_rue, rue, code_postal, ville):

    with open("immobiliers/Proprietes_données.json", 'r') as f:
        history_imobiliers = json.loads(f.read())

    pro_recherche = None
    for pro in history_imobiliers:
        if pro['n_rue'] == num_rue and pro['bld/rue/impasse'] == rue and pro['ville'] == ville and pro[
            'numero_appt'] == num_appt and int(pro['code_postal']) == code_postal:
            return pro


def calculate_property_appraisal_score(property_info):
    size_m2 = property_info['size_m2']
    location = property_info['location']
    year_built = property_info['year_built']
    bedrooms = property_info['bedrooms']
    bathrooms = property_info['bathrooms']
    size_score = size_m2 / 300
    location_score = {'A': 0.9, 'B': 0.8,
                      'C': 0.7, 'D': 0.6}.get(location, 0.5)
    age_score = (2023 - year_built) / 100
    bedrooms_score = bedrooms / 5
    bathrooms_score = bathrooms / 4
    property_score = (size_score + location_score +
                      age_score + bedrooms_score + bathrooms_score) / 5

    return property_score, property_info['prix']


@app.post("/calcul-score-pro")
async def calcul_score_prop(immobilier: ImmobilierModelProp = Body()):
    immobilier = immobilier.model_dump()
    property_find = find_propriete(immobilier["num_appt"],
                                   immobilier["num_rue"],
                                   immobilier["rue"],
                                   immobilier["code_postal"],
                                   immobilier["ville"]
                                   )
    property_score, property_info = calculate_property_appraisal_score(property_find)
    return {
        "property_score": property_score,
        "prix": property_info
    }
