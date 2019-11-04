#5
#def printName():
#    print("Paweł Ważydrąg")

#6
#def uek():
#    print("Uniwersytet Ekonomiczny w Krakowie")
#    print("ul. Rakowicka 27")
#    print("31-510 Kraków")

#7
def cyfry():
    a = 0
    for z in range (0,3):
        for zz in range (0,3):
            a += 1
            print(a, end=" ")
        print()
cyfry()
#8
print()
x=3
def f():
    x=1
f()
print(x)
print()

#9
def f():
    s = "I love Disco Polo!"
    print(s)

s="I love Rock & Roll"
f()
print(s)
print()

#10
#y=2x+2
#x=3 y=7 z= 2x+2 + x + y = 18
def f():
    y = x + 2
    return x + y
x = 3
y = x + 4
z = f() + x + y
print(x, y, z)
print()
#11
def f():
    x = y
    x[1] = y[0] + x[1]
x = [1,2,3]
y = [4,5]
f()
print(x,y)
print()
#12
def iloczyn(a,b):
    print(a*b)
    
iloczyn(10,3)
print()
#13
tab=[4,3,7,1,3]
def suma(tablica):
    sum=0
    for w in tablica:
        sum += w
    print(f"Suma wartości: {sum}")
print(tab)
suma(tab)
print()

#14
def wystepuje(liczba,tablica):
    if liczba in tablica:
        print("Ta liczba znajduje się w tablicy.")
    else:
        print("Nie ma tej liczby w tej tablicy.")
tab2=[13,38,7,23,14]
wystepuje(23,tab2)
print()
#15
def multiplication(k,m):
    return k*m

print(multiplication(3,4))
print()
#16
def czytajLiczbe():
    q = int(input("Wpisz pierwszą liczbę: "))
    r = int(input("Wpisz drugą liczbę: "))
    suma = q + r
    return f"Ich suma to: {suma}"
print(czytajLiczbe())
print()
#17
import random
def rzucKostka():
    e=random.randint(1,6)
    return e
print("Wyrzucone liczby: ",end="")
suma=0
for l in range (0,3):
    v=rzucKostka()
    print(v,end=" ")
    suma+=v
print()
print(f"Suma tych liczb to: {suma}")
print()
#18
def silnia(n):
    #0!=1 oraz 1!=1
    if n==0 or n==1:
        return 1
    #n! = n * (n-1)!
    if n > 1:
        return n * silnia(n-1)
print( f"10! = {silnia(10)}" )
print()
#19
def sumaa(N):
    if N == 1:
        return 1
    elif N>1:
        return N + sumaa(N-1)

print(sumaa(10))
print()
#20
def potega(x,n):
    if n == 1:
        return x
    elif n > 1:
        return x * potega(x,n-1)
    
print(potega(5,3))
print()