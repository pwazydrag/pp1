def czytajWspolczynniki():
    tab=[]
    a=float(input("Podaj współczynnik a: "))
    b=float(input("Podaj współczynnik b: "))
    c=float(input("Podaj współczynnik c: "))
    tab.append(a)
    tab.append(b)
    tab.append(c)
    return tab
def obliczDelte(tab):
    delta=tab[1]*tab[1]-4*tab[0]*tab[2]
    return delta
def obliczPierwiastki(tab):
    tabx1x2=[]
    delta=obliczDelte(tab)
    if delta < 0:
        return tabx1x2
    elif delta==0:
        x1=-1*tab[1]/2*tab[0]
        tabx1x2.append(x1)
        return tabx1x2
    elif delta>0:
        pdelta=delta**(1/2)
        x1 = (-1 * pdelta + -1 * tab[1]) / 2*tab[0]
        x2 = (pdelta + -1 * tab[1]) / 2*tab[0]
        tabx1x2.append(x1)
        tabx1x2.append(x2)
        return tabx1x2
def wyswietlPierwiastki(tabx1x2):
    if len(tabx1x2)==1:
        print(f"Istnieje jeden pierwiastek: {tabx1x2[0]}")
    elif len(tabx1x2)==0:
        print("Nie ma pierwiastków.")
    elif len(tabx1x2)==2:
        print(f"Istnieją dwa pierwiastki: {tabx1x2[0]} oraz {tabx1x2[1]}")
#wyswietlPierwiastki(obliczPierwiastki(czytajWspolczynniki()))
