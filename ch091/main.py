from Rectangle import Rectangle


def main():
    r = Rectangle(1,2)
    r1 = Rectangle(12,2)

    r.longueur = 12
    #r.set_longueur(12)
    print(r.longueur)
    #l = r.get_longueur(12)

    assert r.longueur ==12

    # r.set_longueur(12)
    r.longueur = 12
    assert r.longueur ==12
    print(r.surface)

    s = str(r)
    print(s)

    print(int(r))
    # if r.__eq__(r1):
    if r == r1:
        print("ok")
    else:
        print("ko")
    
    print(50*"-")
    r2 = Rectangle(15,88)
    print(Rectangle.get_cpt())
    del r2
    print(50*"-")

    print(Rectangle.get_cpt())
    print("la fin")

if __name__=='__main__':
    main()
