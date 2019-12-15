class Student():
    def __init__(self, imie, nazwisko, numer):
        self.imie =imie
        self.nazwisko=nazwisko
        self.numer = numer
    def __eq__(self, other):
        return self.numer == other.numer
    def __lt__(self, other):
        return self.numer <= other.numer
    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.numer}"
    
s1=Student("Anna", "Tomaszewska", 141820)
s2=Student("Wojciech", "Zbych", 201003)
s3=Student("Maja", "Kowalska", 153202)
s4=Student("Marek", "Migiel", 138600)
print(s1, s2, s3, s4, sep="\n")
print()
t=[s1,s2,s3,s4]
tab=sorted(t, key=lambda Student:Student.numer)
for v in tab:
    print(v)