class Kontakt():
    def __init__(self, nazwa, email, telefon):
        self.nazwa=nazwa
        self.email=email
        self.telefon=telefon
        self.dane=[]
    def zwrocKontakt(self):
        self.dane.append(self.nazwa)
        self.dane.append(self.email)
        self.dane.append(self.telefon)
        return self.dane
    def wyswietlKontakt(self):
        print(*self.dane,sep='\t\t')

class ListaKontaktow():
    def __init__(self):
        self.kontakty=[]
    def dodajKontakt(self, newKontakt):
        self.kontakty.append(newKontakt)
    def wyswietlKontakty(self):
        for v in self.kontakty:
            if isinstance(v, list):
                for w in v:
                    print(f"{w:<18}", end="")
                print()
            
kon1=Kontakt("Kowalski Jan", "jank@onet.pl", 55523400)
kon2=Kontakt("Borek Patrycja","bp@o2.pl", 232000199)
kon3=Kontakt("Maj Piotr", "maj@google.pl", 2229991000)
kon4=Kontakt("Adamczyk Anna", "ada@poczta.pl", 100200300)
lista=ListaKontaktow()
lista.dodajKontakt(kon1.zwrocKontakt())
lista.dodajKontakt(kon2.zwrocKontakt())
lista.dodajKontakt(kon3.zwrocKontakt())
lista.dodajKontakt(kon4.zwrocKontakt())
lista.wyswietlKontakty()

        