class Kostka():
    def __init__(self):
        self.wynik=0
    def rzucKostka(self):
        import random
        self.wynik=random.randint(1,6)
    def zwrocWynik(self):
        return self.wynik
    
kos1=Kostka()
kos2=Kostka()
kos3=Kostka()
kos1.rzucKostka()
kos2.rzucKostka()
kos3.rzucKostka()
print(kos1.zwrocWynik())
print(kos2.zwrocWynik())
print(kos3.zwrocWynik())
suma=kos1.zwrocWynik() + kos2.zwrocWynik() + kos3.zwrocWynik()
print(f"Suma wyrzuconych oczek wynosi: {suma}")