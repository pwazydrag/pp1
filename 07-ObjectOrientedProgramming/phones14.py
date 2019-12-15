class Phone():
    def __init__(self, firma, kolor, numer):
        self.firma=firma
        self.kolor=kolor
        self.numer=numer
        self.blokada=True
    def odblokuj(self):
        if self.blokada==True:
            self.blokada=False
            print("Telefon odblokowany.")
        else:
            print("Telefon jest już odblokowany.")
    def zablokuj(self):
        if self.blokada==False:
            self.blokada=True
            print("Telefon zablokowany pomyślnie.")
        else:
            print("Telefon jest już zablokowany.")
    def zadzwoń(self, numer):
        if self.blokada==False:
            print(f"Dzwonię pod numer {numer}...")
        else:
            print("Najpierw odblokuj telefon!")
    def __str__(self):
        return f"Telefon firmy {self.firma}, koloru {self.kolor}, o numerze {self.numer}"
t1=Phone("Xiaomi", "niebieski", "66745723")
t2=Phone("Samsung", "czarny", "612341523")
print(t1)
print(t2)
t1.odblokuj()
t1.zadzwoń(123456789)
t1.zablokuj()
t1.zadzwoń(123456789)
