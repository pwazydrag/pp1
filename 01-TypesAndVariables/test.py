import math
import random

#NWD 2 LICZB
#a=int(input())
#b=int(input())
#print(math.gcd(a,b))

k=random.randint(1,6)
m=random.randint(1,6)
n=random.randint(1,6)
print(k, m, n, k + m + n)

x=random.randint(1,6)
y=int(input())
if x==y:
    print("Jesteś kozakiem brawo")
else:
    print("Następnym razem")
    print(f"Komputer wyrzucił : {x}")
    
tablica=[12,6,4,9,10]
for i in range(0, tablica[0]):
    print("*", end=" ")
print("")
    
for i in range(0, tablica[1]):
    print("*", end=" ")
print("")
    
for i in range(0, tablica[2]):
    print("*", end=" ")
print("")
    
for i in range(0, tablica[3]):
    print("*", end=" ")
print("")
    
for i in range(0, tablica[4]):
    print("*", end=" ")
print("")