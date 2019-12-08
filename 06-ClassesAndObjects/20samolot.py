class lot():
    def __init__(self, numer_lotu, cel):
        self.numer_lotu=numer_lotu
        self.prędkość=0
        self.wysokość=0
        self.cel = cel
        self.lot=False
        self.koniec=False
    def początekLotu(self, wysokosc):
        self.lot=True
        if wysokosc>=1000 and wysokosc <= 2000:
            self.wysokość=wysokosc
        else:
            print("Nieodpowiednia wysokość startowa.")
    def zmianaWysokosci(self, newwysokosc):
        if newwysokosc >= 300 and newwysokosc <= 11000:
            self.wysokość=newwysokosc
        else:
            print("Niebezpieczna wysokość! Nie możesz lecieć na tej wysokości.")
    def Lądowanie(self):
        if self.wysokość>=500:
            print("Nie możesz lądować przy tej wysokości!")
        else:
            self.lot=False
            self.koniec=True
    def statusLotu(self):
        if self.lot==False and self.koniec==True:
            print(f"Tutaj {self.numer_lotu}. Wylądowałem w miejscu docelowym.")
        elif self.lot==False and self.koniec==False:
            print(f"Tutaj {self.numer_lotu}. Nie rozpocząłem jeszcze lotu.")
        else:
            print(f"Tutaj {self.numer_lotu}. Znajduję się na wysokości {self.wysokość}m.")

mójLot=lot("LOT881","Berlin")
mójLot.statusLotu()
mójLot.początekLotu(1500)
mójLot.statusLotu()
mójLot.zmianaWysokosci(8900)
mójLot.statusLotu()
mójLot.zmianaWysokosci(200)
mójLot.statusLotu()
mójLot.Lądowanie()
mójLot.statusLotu()
mójLot.zmianaWysokosci(400)
mójLot.statusLotu()
mójLot.Lądowanie()
mójLot.statusLotu()