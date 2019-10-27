#36
szuk=0
while True:
    szuk= szuk + 1
    if szuk % 7 == 0 and szuk % 2 == 1 and szuk % 3 == 1 and szuk % 4 == 1 and szuk % 5 == 1 and szuk % 6 == 1:
        print(f"Ta liczba to: {szuk}. ")
        break
    else:
        continue
    

#37
a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))
c=int(input("Podaj trzecią liczbę: "))
if a > b and a > c and b > c:
    mediana=(a+c)/2
elif a > b and a > c and b < c:
    mediana=(a+b)/2
elif a > b and a < c and b < c:
    mediana=(b+c)/2
elif a > c and a < b and b > c:
    mediana=(b+c)/2
elif c>b and c>a and b>a:
    mediana=(a+c)/2
else:
    mediana=(a+b)/2
print(mediana)

#38
#for i in range(6,-1,-3):
#    for j in range(1,4):
#        print(f' {i+j}',end='')
#    print()
i=6
j=1
while (i>=0):
    while(j != 4):
        print(f"{i+j}", end="")
        j = j + 1
    print()
    j = 1
    i = i - 3
    
#39
x=0
y=1
print(x,y, end=" ")
for xyz in range(0,23):
    x = x + y
    y = x + y
    print(x,y, end=" ")
print()
    
#41
suma=0
ilosc=0
while True:
    x=int(input("Podaj liczbę: "))
    if x!=0:
        ilosc=ilosc + 1
        suma = suma + x
        średnia=suma/ilosc
    if x==0:
        break
print(f"suma wynosi: {suma}, natomiast średnia: {średnia}")

#40
import random
jeden = 0
dwa = 0
trzy = 0
cztery = 0
pięć = 0
sześć = 0
for zyx in range (0,100):
    r = random.randint(1,6)
    if r == 1:
        jeden = jeden + 1
    elif r ==2:
        dwa = dwa + 1
    elif r == 3:
        trzy = trzy + 1
    elif r==4:
        cztery = cztery + 1
    elif r==5:
        pięć = pięć + 1
    else:
        sześć = sześć + 1
print(f"Jedynki: {jeden}, dwójki: {dwa}, trójki: {trzy}, czwórki: {cztery}, piątki:{pięć}, szóstki: {sześć}")