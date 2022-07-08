
class Rectangle:

    _cpt = 0

    def __init__(self,longueur:int,largeur:int) -> None:
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt+=1


    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur

    def set_longueur(self,longueur):
        self._longueur = longueur

    def set_largeur(self,largeur):
        self._largeur = largeur

    def get_surface(self):
        return self._longueur*self._largeur

    def get_cpt():
        return __class__._cpt

    def __str__(self) -> str:
        return f"{__class__.__name__} {self._longueur=}, {self._largeur=}"

    def __int__(self):
        return self.get_surface()

    def __eq__(self, __o: object) -> bool:
        return self._longueur == __o._longueur and self._largeur == __o._largeur

    def __del__(self):
        print("def __del__(self)")
        Rectangle._cpt-=1
