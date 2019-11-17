#33
def fib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a
for f in range (1,20):
    print(fib(f),end=" ")
print()
print()
#34
def fib34(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fib34(n-1)+fib34(n-2)      
print(fib34(6))
print()
for F in range (1,21):
    print(fib34(F))
print()
#35
liczba=12345
def summary(num):
    k = num % 10
    if num < 1:
        return 0
    elif num >=1:
        return k+summary(num//10)
print(summary(liczba))
print()
#36
tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
def summary36(tablica):
    suma=0
    for l in tablica:
        if isinstance(l,list):
            suma = suma + summary36(l)
        else:
            suma = suma + l
    return suma
print(summary36(tab))