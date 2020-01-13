class Stos:
    def __init__(self):
        self.t=[]
    def wstaw(self, nazwa_karty):
        self.t.append(nazwa_karty)
    def jest_pusty(self):
        return len(self.t)>0
    def zdejmij(self):
        if Stos.jest_pusty(self):
            pom = self.t[-1]
            del self.t[-1]
            print(f"Zdejmuję {pom} ze stosu.")
    def __str__(self):
        return f"Zawartość stosu: {self.t}"

s=Stos()
s.wstaw(2)
s.wstaw(3)
s.wstaw(5)
s.wstaw("as")
print(s)
s.zdejmij()
print(s)
s.zdejmij()
print(s)
s.zdejmij()
print(s)
s.zdejmij()
print(s)
s.zdejmij()
print(s)