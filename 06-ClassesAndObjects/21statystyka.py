class Statystyka():
    def __init__(self):
        self.tab=[]
    def dodajLiczbe(self):
        self.tab.append(int(input("Podaj liczbę którą chcesz dodać: ")))
    def pokazWszystkieLiczby(self):
        if len(self.tab)>0:
            print(self.tab)
        else:
            print("Nie ma żadnych liczb.")
    def pokazMaximum(self):
        lmax=0
        if len(self.tab)>0:
            lmax=self.tab[0]
            for v in self.tab:
                if v>lmax:
                    lmax=v
        print(f"Liczba największa to: {lmax}")
    def pokazMinimum(self):
        lmin=0
        if len(self.tab)>0:
            lmin=self.tab[0]
            for w in self.tab:
                if w<lmin:
                    lmin=w
        print(f"Liczba najmniejsza to: {lmin}")
    def pokazSredniaArytm(self):
        srednia=0
        suma=0
        if len(self.tab)>0:
            for p in self.tab:
                suma+=p
            srednia=suma/len(self.tab)
        print(f"Średnią tego zbioru liczb jest: {srednia}")
    def pokazMediane(self):
        mediana=0
        if len(self.tab)>0:
            if len(self.tab)%2==1:
                self.tab.sort()
                pom=len(self.tab)//2
                mediana=self.tab[pom]
                print(f"Mediana tego zbioru to: {mediana}")
            elif len(self.tab)%2==0:
                self.tab.sort()
                pom1=len(self.tab)//2-1
                pom2=len(self.tab)//2
                pom1w=self.tab[pom1]
                pom2w=self.tab[pom2]
                mediana=(pom1w+pom2w)/2
                print(f"Mediana tego zbioru to: {mediana}")
myStats=Statystyka()
myStats.pokazWszystkieLiczby()
myStats.dodajLiczbe()
myStats.dodajLiczbe()
myStats.dodajLiczbe()
myStats.dodajLiczbe()
#myStats.dodajLiczbe()
myStats.dodajLiczbe()
myStats.pokazWszystkieLiczby()
myStats.pokazMaximum()
myStats.pokazMinimum()
myStats.pokazSredniaArytm()
myStats.pokazMediane()
