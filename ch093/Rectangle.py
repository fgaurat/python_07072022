from ICalcGeo import ICalcGeo


class Rectangle(ICalcGeo):

    _cpt = 0

    def __init__(self,longueur:int,largeur:int) -> None:
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt+=1


    @property
    def longueur(self):
        return self._longueur
    
    @property
    def largeur(self):
        return self._largeur

    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur

    @property
    def surface(self):
        return self._longueur*self._largeur

    def get_cpt():
        return __class__._cpt

    def __str__(self) -> str:
        return f"{__class__.__name__} {self._longueur=}, {self._largeur=}"

    def __int__(self):
        return self.surface

    def __eq__(self, __o: object) -> bool:
        return self._longueur == __o._longueur and self._largeur == __o._largeur

    def __del__(self):
        print("def __del__(self)")
        Rectangle._cpt-=1
