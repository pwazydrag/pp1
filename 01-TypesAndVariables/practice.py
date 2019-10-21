import math

liczba=21
print(f"Wartość liczby to {liczba}, a {liczba**2} to jej druga potęga")

wiek=19
imię="Paweł"
wzrost=169
print(f"Mam na imię {imię} i mam {wiek} lat, a mój wzrost to {wzrost} cm ")

Kwota=15.84
VAT=(Kwota * 0.23)
print("{:.3}".format(VAT))

#uczelnia = "Uniwersytet Ekonomiczny w Krakowie"
#x = "wersyt" in uczelnia
#print(x)

nazwisko="Ważydrąg"
print(imię + " " + nazwisko)

#x=int(input())

r=5
długość=r * math.pi * 2
print(długość)
pole= r**2 * math.pi
print(pole)

temperaturaC=float(input())
temperaturaK=temperaturaC + 273
print(temperaturaK)
temperaturaF=(9/5)*temperaturaC + 32
print(temperaturaF)

a=float(input())
b=float(input())
c=float(input())
połowa = (a+b+c)/2
PoleHeron = (połowa*(połowa-a)*(połowa-b)*(połowa-c))**(1/2)
print(PoleHeron)

centymetry=float(input())
stopy=centymetry / 30.48
print(stopy)

numer=str(input())
print(numer[0:2] + " " + numer[2:6] + " " + numer[6:10] + " " + numer[10:14] + " " + numer[14:18] + " " + numer[18:22] + " " + numer[22:26] + " " + numer[26:30])

wzrostBMI=float(input())
wagaBMI=float(input())
WskaźnikBMI= wagaBMI / (wzrostBMI**2)
print(WskaźnikBMI)