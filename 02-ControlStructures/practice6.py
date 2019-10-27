#45

n=int(input("Wprowadź do której liczby chcesz wyświetlić liczby pierwsze: "))
print(2)
for w in range (2,n+1):
    for u in range (2,w):
        if w % u == 0:
            break
        elif w % u !=0:
            if u == w -1:
                print(w)
                break
            else:
                continue

#46
import random
liczby=[]
for z in range (0,20):
    x=random.randint(-20,-5) 
    liczby.append(x)
print(liczby)

#47
kwota=int(input("Podaj kwotę w zł: "))
z5=kwota//5
z2=(kwota-z5*5)//2
z1=kwota - z5*5 - z2*2
print(f"5zł - {z5}, 2zł - {z2}, 1zł - {z1}")

#48
a=1
b=0
for v in range (0,7):
    for h in range (0,7):
        print(a, end=" ")
        a = a + 7
    b = b +1
    a=1
    a=a + b
    print()
    
