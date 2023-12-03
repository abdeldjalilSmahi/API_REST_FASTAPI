# from fastapi import FastAPI, Body, Request
# # from fastapi.responses import PlainTextResponse
# # import os
# # import time
# # from server.models.demande import Demande
# # from server.models.information import Information
# # from server.baseModels.information_model import InformationModel, InformationFinanciereClient, InformationPersonnelleClient
# #
# # import os
# # import json
# # import requests
# # from pydantic import BaseModel
# #
# #
#
# ## 127.0.0.1:8002
# app = FastAPI()
#
#
# # Obtenez le chemin absolu du répertoire 'server'
# server_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Changez le répertoire de travail vers le répertoire 'server'
# os.chdir(server_dir)
#
# # Maintenant vous pouvez utiliser des chemins relatifs par rapport à 'server'
#
#
#
#
#
# # @app.post("/approbation")
# # async def approbation_demande(informationModel: InformationModel = Body()):
# #
# #     return informationModel.dict()
#
# @app.get("/verification_solvabilite")
# async def verification_solvabilite_function(historique_client):
#     return {"message" : f"{historique_clients}"}
#
# # @app.get("/historique_clients/{client_id}")
# # async def recuperation_historique_client(client_id):
# #     with open(f"historique_clients/{client_id}.json", 'r') as file:
# #         historique_client = json.load(file)
# #
# #     return historique_client["historique"]