#24
a=0
miesiące=["styczeń","luty","marzec","kwiecień","maj","czerwiec","lipiec","sierpień","wrzesień","październik","listopad","grudzień"]
def miesiąc():
    b=int(input("Podaj liczbowe oznaczenie miesiąca: "))
    a = b - 1
    print()
    return miesiące[a]

print(miesiąc())
print()

#25
Imiona=["Janek","Ania","Wojtek","Zosia"]
def jestImie(imie,imiona):
    if imie in imiona:
        print("Imię jest zawarte.")
    else:
        print("Nie ma tego imienia.")

jestImie("Ania",Imiona)
#26
def podatek(dochod):
    if dochod<=5000:
        pod=0.17*dochod
        return f"Podatek wynosi: {pod} zł."
    elif dochod>5000:
        pod=0.17*5000+(dochod-5000)*0.32
        return f"Podatek wynosi {pod} zł."
print(podatek(6000))
print()
#27
reduta="Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem napole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
import re
def samogłoska():
    a=re.findall('[a]',reduta)
    aa=re.findall('[ą]',reduta)
    e=re.findall('[e]',reduta)
    ee=re.findall('[ę]',reduta)
    y=re.findall('[y]',reduta)
    u=re.findall('[u]',reduta)
    uu=re.findall('[ó]',reduta)
    o=re.findall('[o]',reduta)
    i=re.findall('[i]',reduta)
    return f"Liczba występowań poszczególnych samogłosek: a: {len(a)}, ą: {len(aa)}, e: {len(e)}, ę: {len(ee)}, y: {len(y)}, u: {len(u)}, o: {len(o)}, ó: {len(uu)}, i: {len(i)}\n"
print(samogłoska())
#28
lang=["Java","Python","JavaScript","C++","C#","Ruby","Perl","PHP","C","Android"]
stats=[61,47,37,32,26,18,14,14,9,7]
def rysujWykres(jezyki,wartosci):
    a = 0
    for w in range (0,len(lang)):
        print(jezyki[a]+": ", end="\t\t")
        for ww in range (0,wartosci[a]):
            print("#",end="")
        a += 1
        print()
rysujWykres(lang,stats)