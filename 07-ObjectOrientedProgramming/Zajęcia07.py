''' #4
class University():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name + "is the best!"
my_university = University('UEK Kraków')
print(my_university)
'''
#5
class Song():
    def __init__(self, wykonawca, tytuł, album, rok):
        self.wykonawca=wykonawca
        self.tytuł=tytuł
        self.album=album
        self.rok=rok
    def __str__(self):
        return f"{'Wykonawca:':<10} {self.wykonawca}\n{'Tytuł:':<10} {self.tytuł}\n{'Album:':<11}{self.album}\n{'Rok:':<10} {self.rok}"
fancy=Song("Twice","Fancy","Fancy You",2019)
print(fancy)
#7
class Student():
    numer=100000
    def __init__(self, imie, nazwisko, kierunek):
        self.imie=imie
        self.nazwisko=nazwisko
        self.kierunek=kierunek
        self.numer=Student.numer
        Student.numer+=1
        self.uczelnia="UEK Kraków"
    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.numer}), {self.kierunek}, {self.uczelnia}."
        
u1=Student("Adam", "Kowalski", "Informatyka")
print(u1)
u2=Student("Paweł","Nowak", "Informatyka")
print(u2)

#message.py
#SMS
#EMAIL
#teraz 10 trzeba zrobić
