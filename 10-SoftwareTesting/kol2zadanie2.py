class Miasto:
    def __init__(self, nazwa, populacja):
        self.nazwa = nazwa
        self.populacja = populacja
    def __str__(self):
        return f"{self.nazwa} ({self.populacja})"

Zakopane = Miasto("Zakopane", 27000)
Gdynia = Miasto("Gdynia",246000)
print(Zakopane)
print(Gdynia)