#16
i = 0
for i in range (0,10):
    i = i + 1
    print(1/i)
    
#17
j=0
sumaparzystych=0
sumanieparzystych=0
for j in range (1,51):
    if j % 2 == 0:
        sumaparzystych = sumaparzystych + j
    else:
        sumanieparzystych = sumanieparzystych + j
        
print(sumaparzystych,sumanieparzystych)

#18

for k in range (1,31):
    if k % 3 == 0 and k % 5 == 0:
        print("BINGO!")
    elif k % 3 == 0 and k % 5 != 0:
        print("THREE")
    elif k % 3 != 0 and k % 5 == 0:
        print("FIVE")
    else:
        print(k)
        
#19
m=1
N=int(input("Ile początkowych wyrazów ciągu chcesz wyświetlić? "))
for u in range (0,N):
    print(m, end = " ")
    m = m + 3
#24
tablicaimiona=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]
r = 0
for z in tablicaimiona:
    p = len(z)
    if p > r:
        r = p
        wynik = z
    elif p < r or p == r:
        r = r

print(f"Najdluzsze imię: {wynik}, jego liczba liter to: {r}")
    
#25
for aaa in range (0,3):
    for bbb in range (0,7):
        print("*" , end = " ")
    print()


    
    