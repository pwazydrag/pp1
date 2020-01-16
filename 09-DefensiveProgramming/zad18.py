imie0=input("Podaj imię: ")
nazwisko0=input("Podaj nazwisko: ")
assert len(imie0)>3, "Imię jest za krótkie."
assert len(nazwisko0)>3, "Nazwisko jest za krótkie."
imie1=imie0[0]
imie2=imie0[1:]
imie1 = imie1.upper()
imie2 = imie2.lower()

nazwisko1 = nazwisko0[0]
nazwisko2 = nazwisko0[1:]
nazwisko1 = nazwisko1.upper()
nazwisko2 = nazwisko2.lower()
print(f"{imie1}{imie2} {nazwisko1}{nazwisko2}")

