class ulamek():
    def __init__(self,licznik,mianownik):
        self.licznik=licznik
        self.mianownik=mianownik
    def nowylicznik(self, newl):
        self.licznik=newl
    def nowymianownik(self, newm):
        self.mianownik=newm
    def uproszczenie(self):
        for v in range (1,self.mianownik+1):
            if self.mianownik%v == 0 and self.licznik%v==0:
                self.licznik=self.licznik//v
                self.mianownik=self.mianownik//v
    def wyswietl(self):
        print(str(self.licznik) + "/" + str(self.mianownik))
czteryosiem=ulamek(4,8)
czteryosiem.uproszczenie()
czteryosiem.uproszczenie()
czteryosiem.wyswietl()
