#11 #12
wiek = 24
if type(wiek) != int:
    raise TypeError('Wiek powinien być liczbą całkowitą!')
if wiek>120 or wiek <0:
    raise ValueError("Niemożliwe!")
print(f'Masz {wiek} lat')

#13
cena_netto = 16.2
if (type(cena_netto) != float) and (type(cena_netto) !=int):
    raise TypeError('Cena powinna być liczbą!')
if cena_netto<0:
    raise ValueError("Cena nie może być mniejsza od 0!")
cena_brutto=cena_netto*1.23
print(round(cena_brutto, 2), "zł")

#14
def pole_prostokata():
    try:
        a=float(input("Wprowadź dł. pierwszego boku: "))
        b=float(input("Wprowadź dł. drugiego boku: "))
    except:
        raise TypeError("Długości boków muszą być liczbami!")
        
    if a<0 or b<0:
        raise ValueError("Boki nie mogą mieć długość mniejszej od 0!")
    pole = a * b
    return pole
print(pole_prostokata())