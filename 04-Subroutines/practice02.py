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

#27
reduta="Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem napole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
def samogłoska():
    a=0
    for e in reduta:
        a+=1
        return a
    ??????
print(samogłoska())