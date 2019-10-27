#31
b=0
uczelnia = "UEK w Krakowie"
for b in uczelnia:
    print(b , end = " ")
print()
    
#32
a=str(input("Wpisz ciąg znaków. "))
b=a[::-1]
print(b)

#33
liczba=38227
cyfry=["zero", "jeden","dwa","trzy","cztery","pięć","sześć","siedem", "osiem", "dziewięć"]
liczbasłownie=[]
for w in str(liczba):
    cyfra = cyfry[int(w)]
    liczbasłownie.append(cyfra)
print(*liczbasłownie, sep=", ")

#34
pesel=str(input("Podaj PESEL: "))
if pesel[9] == "1" or pesel[9] == "3" or pesel[9] == "5" or pesel[9] == "7" or pesel[9] == "9":
    print("Płeć męska. ")
else:
    print("Płeć żeńska. ")
e=int(pesel[0])
f=int(pesel[1])
if e == 0:
    wiek = 19 -f
    print(wiek)
else:
    wiek = 100 - (10*e + f) + 19
    print(wiek)
    
#35
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
c=float(input("Podaj c: "))
delta= b**2 - 4*a*c
pdelta=delta**(1/2)
if delta > 0:
    x1 = (-b -pdelta)/2
    x2 = (-b +pdelta)/2
    print(f"Miejsca zerowe to: {x1}, {x2}. ")
elif delta == 0:
    x1 = -b / 2*a
    print(f"Istnieje jedno miejsce zerowe: {x1}")
else:
    print("Nie ma miejsc zerowych.")