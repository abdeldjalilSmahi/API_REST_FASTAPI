from fastapi import Body, FastAPI
from models.persistor import Persistor
from models.demande import Demande
from pydantic import BaseModel
from models.client import Client
from baseModels.demade_model import DemandeModel
from models.immobilier import Immobilier
app = FastAPI()
## 127.0.0.1:8000 car c'est la première
@app.post("/demandes")
async def reception_demande(nouvelle_demande: DemandeModel = Body()):
    demande = Demande(**nouvelle_demande.dict())
    client = Client(**nouvelle_demande.client.dict())  # Correction ici
    immobilier = Immobilier(**nouvelle_demande.immobilier.dict())
    id_client = client.id
    persistor = Persistor(id_client)
    persistor.save_demande(demande)
    return {"message": "Nous avons bien enregistré votre demande, vous recevez une réponse le plus tôt possible"}

