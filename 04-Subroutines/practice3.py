#29
import statistics
import collections
import random
tab=[4,4,4,4,4,1,1,1,1,1,2,2,2,2,2,3,7]

def mediana(tablica):
    tablica.sort()
    if len(tablica) % 2 != 0:
        pom = len(tablica)//2
        med = tab[pom]
        return med
    elif len(tablica) % 2 == 0:
        pom1 = len(tablica)//2
        pom2 = pom1 - 1
        med = (tab[pom1]+tab[pom2])/2
        return med
#       return statistics.median(tablica) <---- o wiele prościej

print(mediana(tab))
print()
def dominanta(tablica):
    #return statistics.mode(tablica)
    licznik=0
    mod=0
    modilosc=1
    modiloscost=0
    modmulti=[]
    tablica.sort()
    for h in tablica:
        licznik +=1
        if licznik!=len(tablica):
            if tablica[licznik]==tablica[licznik-1]:
                modilosc+=1
                if modilosc>modiloscost:
                    mod=h
                    modmulti.clear()
                elif modilosc<modiloscost:
                    continue
                elif modilosc==modiloscost:
                    if len(modmulti)>0:
                        modmulti.append(h)
                    elif len(modmulti)==0:
                        modmulti.append(mod)
                        modmulti.append(h)
            elif tablica[licznik]!=tablica[licznik-1]:
                if modilosc>modiloscost:
                    modiloscost=modilosc
                    modilosc=1                      
                elif modilosc<modiloscost:
                    modilosc=1
                elif modilosc==modiloscost:
                    modilosc=1
        elif licznik==len(tablica):
            break
    if len(modmulti)>0:
        return modmulti
    elif len(modmulti)==0:
        return mod
print(dominanta(tab))
tab.sort()
print(tab)
print()
#30
def los():
    tabpar=[]
    tabnpar=[]
    c=0
    for a in range (0,1000):
        c=random.randint(1,50)
        if c % 2 == 0:
            tabpar.append(c)
        elif c % 2 != 0:
            tabnpar.append(c)
    lenpar=len(tabpar)
    lennpar=len(tabnpar)
    parzproc=lenpar/10
    nparzproc=lennpar/10
    return f" Liczby parzyste: {parzproc} % \n Liczby nieparzyste: {nparzproc} %"
print(los())