from abc import ABC, abstractmethod
class employee(ABC):
    def __init__(self,_nom,_salaire):
        self._nom=_nom
        self._salaire=_salaire
    @property
    def _salaire(self):
        return self.__salaire
    @_salaire.setter
    def _salaire(self,valeur):
        if valeur<0:
            raise ValueError("Le salaire doit etre positif")
        self.__salaire=valeur
    @abstractmethod
    def calcule__salaire(self):
        pass
class employe_horaire(employee):
    def __init__(self,_nom,taux_horaire,heures):
        if heures<0:
            raise ValueError("Le nombre d'heures doit etre positif")
        super().__init__(_nom,taux_horaire)
        self.taux_horaire=taux_horaire
        self.heures=heures
    def calcule__salaire(self):
        return self.taux_horaire * self.heures
class employe_mensuel(employee):
    def __init__(self,_nom,_salaire_fixe):
        super().__init__(_nom,_salaire_fixe)
    def calcule__salaire(self):
        return self._salaire
e1 = employe_horaire("Ali", 80, 160)
print("salaire horaire :", e1.calcule__salaire())

e2 = employe_mensuel("Sara", 5000)
print("salaire mensuel :", e2.calcule__salaire())

e3 = employe_horaire("Zaki", 100, -5)        