
class Client():
    id : int
    nom : str
    prenom : str
    numero_tel : str
    email : str
    depense : float
    revenu : float

    def __init__(self, id, nom, prenom, numero_tel, email, revenu, depense):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.numero_tel = numero_tel
        self.email = email
        self.revenu = revenu
        self.depense = depense

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "numero_tel": self.numero_tel,
            "email": self.email,
            "depense": self.depense,
            "revenu": self.revenu
        }