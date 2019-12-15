class Book():
    def __init__(self, autor, tytuł, rok_wydania):
        self.autor=autor
        self.tytul=tytuł
        self.rok_wydania=rok_wydania
        
class TraditionalBook(Book):
    def __init__(self, ilosc_stron):
        self.ilosc_stron=ilosc_stron
    def __str__(self):
        return f"Książka papierowa autorstwa {self.autor}, o tytule {self.tytul}, wydana w roku {self.rok_wydania}, posiadająca {self.ilosc_stron} stron."

TraditionalBook