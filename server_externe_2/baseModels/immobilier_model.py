from pydantic import BaseModel


class ImmobilierModelProp(BaseModel):
    num_appt: int
    num_rue: int
    rue: str
    code_postal: int
    ville: str
