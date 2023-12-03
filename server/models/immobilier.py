class Immobilier :
    num_appt: int
    num_rue: int
    rue: str
    code_postal: int
    ville: str

    def __init__(self, num_appt, num_rue, rue, code_postal, ville):
        self.num_appt = num_appt
        self.num_rue = num_rue
        self.rue = rue
        self.code_postal = code_postal
        self.ville = ville

    def to_dict(self):
        return {
            "num_appt": self.num_appt,
            "num_rue": self.num_rue,
            "rue": self.rue,
            "code_postal": self.code_postal,
            "ville": self.ville
        }