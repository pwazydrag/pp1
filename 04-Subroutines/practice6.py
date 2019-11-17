#37
tab=[1,2,2,2,2,2,2,3,3,4,3,4,5,6,2,4,6,10,12,14]
def norepeat(tablica):
    tabused=[]
    tab2=[]
    for w in tablica:
        if w not in tabused:
            if w in tab2:
                tab2.remove(w)
                tabused.append(w)
            elif w not in tab2:
                tab2.append(w)
        elif w in tabused:
            continue
    return tab2
print(norepeat(tab))
print()
#38
txt="Nazywam się Jan Kowalski. Pochodzę z Krakowa. Lubię IT"
def wielkielitery(string):
    txtost=[]
    import re
    txtost=re.findall('[A-Z]',string)
    return txtost
print(*wielkielitery(txt),sep="")
print()
#39
def isNin():
    x=int(input("Podaj początek przedziału: "))
    y=int(input("Podaj koniec przedziału: "))
    N=int(input("Podaj liczbę, którą chcesz sprawdzić: "))
    if N>=x and N<=y:
        return "Ta liczba należy do tego przedziału."
    elif N<x:
        return "Ta liczba jest mniejsza od początku przedziału."
    elif N>y:
        return "Ta liczba jest większa od końca przedziału."
print(isNin())
print()

