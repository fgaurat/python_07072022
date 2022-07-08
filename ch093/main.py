from Carre import Carre
from Rectangle import Rectangle
from Cercle import Cercle
from ICalcGeo import ICalcGeo

def affiche_surface(o:ICalcGeo):

    print("surface",o.surface)


def main():
    r = Rectangle(2,5)
    c = Carre(2)
    ce = Cercle(6)

    affiche_surface(r)
    affiche_surface(c)
    affiche_surface(ce)


if __name__=='__main__':
    main()
