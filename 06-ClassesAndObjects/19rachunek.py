class rachunekBankowy():
    def __init__(self, rachuneknumer):
        self.numer_rachunku=rachuneknumer
        self.saldo=0
    def Wplac(self, ilosc):
        self.saldo+=ilosc
    def Wyplac(self, ilosc):
        if ilosc>self.saldo:
            print("Niewystarczająca ilość środków na rachunku.")
        else:
            self.saldo-=ilosc
    def Status(self):
        widoknumeru=""
        widoknumeru+=str(self.numer_rachunku)[0:2]
        poma=2
        pomb=6
        for v in range (0,6):
            widoknumeru+=" "
            widoknumeru+=str(self.numer_rachunku)[poma:pomb]
            poma+=4
            pomb+=4
        print(f"Saldo rachunku bankowego o numerze: {widoknumeru} wynosi {self.saldo} złotych.")


mojnumerrachunku=12345678901234567812345678
mójRachunek=rachunekBankowy(mojnumerrachunku)
mójRachunek.Status()
mójRachunek.Wplac(25.30)
mójRachunek.Status()
mójRachunek.Wyplac(31.70)
mójRachunek.Status()
mójRachunek.Wyplac(14)
mójRachunek.Status()