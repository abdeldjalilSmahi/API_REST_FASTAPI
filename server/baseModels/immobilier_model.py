from pydantic import BaseModel

class ImmobilierModel(BaseModel) :
    num_appt: int
    num_rue: int
    rue: str
    code_postal: int
    ville: str
