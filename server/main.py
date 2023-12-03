# from server.models.client import Client
# from server.models.immobilier import Immobilier
# from server.models.demande import Demande
# from server.models.persistor import Persistor
#
# # Supposons que ces classes sont définies dans le même fichier ou importées correctement.
# # Client, Immobilier, Demande, et Persistor
#
# # Création d'un client
# client = Client(
#     id=2,
#     nom="Dupont",
#     prenom="Jean",
#     numero_tel="0123456789",
#     email="jean.dupont@example.com",
#     revenu=50000.0,
#     depense=20000.0
# )
#
# # Création d'un bien immobilier
# immobilier = Immobilier(
#     num_appt=15,
#     num_rue=20,
#     rue="Raymond Carre",
#     code_postal=94170,
#     ville="Le Perreux"
# )
#
# # Création d'une demande
# demande = Demande(
#     client=client,
#     immobilier=immobilier,
#     montant=300000.0,
#     duree=240
# )
#
# # Création d'un objet Persistor
# persistor = Persistor(id_client=client.id)
#
# # Sauvegarde de la demande
# persistor.save_demande(demande)
#
# # # Lecture des demandes
# # demandes_data = persistor.read_demandes()
# # print(demandes_data)