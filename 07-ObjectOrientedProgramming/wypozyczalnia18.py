class Pojazd():
    def __init__(self, marka, numer_rejestracyjny):
        self.marka=marka
        self.numer_rejestracyjny=numer_rejestracyjny
        self.wypozyczony=False
        self.przebieg=0
    def wypożycz(self):
        if self.wypozyczony==False:
            self.wypozyczony=True
        else:
            print("Ten samochód jest już wypożyczony.")
    def oddaj(self, newprzebieg):
        if self.wypozyczony==True:
            self.wypozyczony=False
            self.przebieg+=newprzebieg
        else:
            print("Nie możesz oddać tego czego nie posiadasz.")
    def zmienPrzebieg(self, new_przebieg):
        self.przebieg=new_przebieg
    def __str__(self):
        return f"Samochód: {self.marka}, numer rejestracyjny: {self.numer_rejestracyjny}, przebieg: {self.przebieg}. "
class Wypożyczalnia():
    def __init__(self, nazwa):
        self.samochody=[]
        self.nazwa= nazwa
    def dodajSamochod(self, pojazd):
        self.samochody.append(pojazd)
    def wyswietlNazwe(self):
        print(f"Wypożyczalnia {self.nazwa}.")
    def wyswietlWszystkieSamochody(self):
        print("Lista wszystkich samochodów:")
        pom=0
        for v in self.samochody:
            pom+=1
            print(pom, end=". ")
            print(v)
        print()
    def wyswietlNiewypożyczoneSamochody(self):
        print("Lista niewypożyczonych samochodów:")
        pom=0
        for v in self.samochody:
            if v.wypozyczony==False:
                pom+=1
                print(pom, end=". ")
                print(v)
        print()
    def wyswietlWypożyczoneSamochody(self):
        print("Lista wypożyczonych samochodów:")
        pom=0
        for v in self.samochody:
            if v.wypozyczony==True:
                pom+=1
                print(pom, end=". ")
                print(v)
        print()
    def zmienStatusWypozyczenia(self, nr_rejestracyjny):
        for v in self.samochody:
            if v.numer_rejestracyjny==nr_rejestracyjny:
                if v.wypozyczony==False:
                    v.wypozyczony=True
                else:
                    v.wypozyczony=False
                        
class Osobowy(Pojazd):
    def __init__(self, marka, numer_rejestracyjny, liczba_miejsc):
        Pojazd.__init__(self, marka, numer_rejestracyjny)
        self.liczba_miejsc=liczba_miejsc
    def __str__(self):
        return(f"Samochód osobowy: {self.marka}, numer rejestracyjny: {self.numer_rejestracyjny}, o liczbie miejsc: {self.liczba_miejsc}, przebieg: {self.przebieg}.")
class Dostawczy(Pojazd):
    def __init__(self, marka, numer_rejestracyjny, ładowność):
        Pojazd.__init__(self, marka, numer_rejestracyjny)
        self.ladownosc=ładowność
    def __str__(self):
        return(f"Samochód dostawczy: {self.marka}, numer rejestracyjny: {self.numer_rejestracyjny}, o ładowności: {self.ladownosc}, przebieg: {self.przebieg}.")
myW=Wypożyczalnia("Mocna Wypożyczalnia")
o1=Osobowy("Golf", "KR12W" , 5 )
o2=Osobowy("Audi", "KR2146V" ,5)
o3=Osobowy("Fiat", "KWI715S", 9)
d1=Dostawczy("Golf", "KWI5125V", 6)
d2=Dostawczy("Fiat", "KR7777CX", 7)
myW.dodajSamochod(o1)
myW.dodajSamochod(o2)
myW.dodajSamochod(o3)
myW.dodajSamochod(d1)
myW.dodajSamochod(d2)
myW.wyswietlWszystkieSamochody()
o1.wypożycz()
d2.wypożycz()
myW.wyswietlWypożyczoneSamochody()
myW.wyswietlNiewypożyczoneSamochody()
o1.oddaj(950)
myW.wyswietlWypożyczoneSamochody()
myW.wyswietlNiewypożyczoneSamochody()
myW.zmienStatusWypozyczenia("KWI715S")
myW.wyswietlWypożyczoneSamochody()
myW.wyswietlNiewypożyczoneSamochody()