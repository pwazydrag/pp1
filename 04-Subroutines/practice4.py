#31
def reverse(tablica):
    a=-1
    revtab=[]
    for w in range (0,len(tablica)):
        revtab.append(tablica[a])
        a-=1
    return revtab
tab=[2, 5, 4, 1, 8, 7, 4, 0, 9]
print(reverse(tab))
print()
#32
macierz1 = [[1, 2, 0], [0, 0, 3], [5, 1, 1]]
print(macierz1)
print()

def widok(macierz):
    for a in macierz:
        print(*a,sep=" ")
    print()
widok(macierz1)

def transpozycja(macierz):
    macierz2=[]
    tabnum=0
    pom=0
    for l in range (0,len(macierz)):
        if tabnum <= len(macierz):
            macierz2.append([])
            if pom!=len(macierz[tabnum]):
                for v in range (0,len(macierz[tabnum])):   
                    macierz2[tabnum].append(macierz[pom][tabnum])
                    pom+=1
                pom=0
            elif pom==len(macierz[tabnum]):
                pom=0
        elif tabnum>len(macierz):
            break
        tabnum +=1
    widok(macierz2)


transpozycja(macierz1)