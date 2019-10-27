#42
a=int(input("Podaj liczbę: "))
b=int(input("Podaj liczbę: "))
if b == 0:
    print("Dzielenie przez 0!!")
else:
    print(a/b)
    
#43
c=int(input("Podaj liczbę: "))
d=int(input("Podaj liczbę: "))
e=int(input("Podaj liczbę: "))
liczby=[c,d,e]
liczby.sort()
print(liczby)

#44
limit=int(input("Podaj limit prędkości (km/h): "))
v=int(input("Podaj prędkość pojazdu (km/h): "))
mandat=0
if v - limit <= 10:
    mandat=5*(v-limit)
else:
    mandat=50+15*(v-limit-10)
print(f"Mandat wynosi: {mandat} złotych.")
    