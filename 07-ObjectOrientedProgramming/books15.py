class Book():
    def __init__(self, autor, tytuł, rok_wydania):
        self.autor=autor
        self.tytul=tytuł
        self.rok_wydania=rok_wydania
        
class TraditionalBook(Book):
    def __init__(self, autor, tytuł, rok_wydania, ilosc_stron):
        self.ilosc_stron=ilosc_stron
        self.autor=autor
        self.tytul=tytuł
        self.rok_wydania=rok_wydania
    def __str__(self):
        return f"Książka papierowa autorstwa {self.autor}, o tytule {self.tytul}, wydana w roku {self.rok_wydania}, posiadająca {self.ilosc_stron} stron."
class EBook(Book):
    def __init__(self, autor, tytuł, rok_wydania, plik):
        self.plik=plik
        self.autor=autor
        self.tytul=tytuł
        self.rok_wydania=rok_wydania
    def __str__(self):
        return f"E-Book, autor: {self.autor}, tytuł: {self.tytul}, rok wydania: {self.rok_wydania}, zapisane w pliku {self.plik}"

tHG=TraditionalBook("Suzanne Collins", "Hunger Games", 2014, 531)
print(tHG)
eHG=EBook("Suzanne Collins", "Hunger Games", 2014, "hg.txt")
print(eHG)