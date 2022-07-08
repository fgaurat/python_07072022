from Carre import Carre
from Rectangle import Rectangle

def affiche_surface(o:Rectangle):

    print("surface",o.surface)


def main():
    r = Rectangle(2,5)
    c = Carre(2)
    print(c.cote)
    print(c)
    print(c.surface)
    print(c.longueur)
    print(c.largeur)
    c.cote = 10
    affiche_surface(r)
    affiche_surface(c)
    affiche_surface(12)


if __name__=='__main__':
    main()