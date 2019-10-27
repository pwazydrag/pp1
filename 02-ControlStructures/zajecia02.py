#8

d=int(input("Wpisz liczbę d: "))
e=int(input("Wpisz liczbę e: "))
if d > e:
    print(d)
elif e > d:
    print(e)
else:
    print("d=e")

#9
z=int(input("Podaj liczbę całkowitą z: "))
if z % 2 == 0:
    print("Ta liczba jest parzysta.")
else:
    print("Ta liczba nie jest parzysta.")


#10
k=int(input("Wprowadź liczbę k: "))
if k % 2 == 1 and k >= 0:
    print("Ta liczba jest nieparzysta oraz dodatnia.")
else:
    print("Ta liczba nie spełnia warunków zadania.")

#11
login=str(input("Podaj login: "))
haslo=str(input("Podaj hasło: "))
if login=="marek" and haslo=="m-123":
    print("Witaj w serwisie.")
else:
    print("Błędne dane.")
    
#12
m=int(input("Wprowadź liczbę m: "))
n=int(input("Wprowadź liczbę n: "))
if m<0 or n<0:
    print("Jedna z tych liczb ma wartość ujemną.")
else:
    print("Żadna z liczb nie spełnia warunków zadania.")
    
#13
x=float(input("Wprowadź wartość x: "))
y=float(input("Wprowadź wartość y: "))
if x>0 and y>0:
    print("Punkt znajduje się w pierwszej ćwiartce.")
elif x>0 and y<0:
    print("Punkt znajduje się w drugiej ćwiartce.")
elif x<0 and y<0:
    print("Punkt znajduje się w trzeciej ćwiartce.")
elif x==0 or y==0:
    print("Punkt znajduje się na jednej z osi.")
else:
    print("Punkt znajduje się w czwartej ćwiartce.")

#14
wiekpsa=float(input("Wprowadź wiek psa: "))
if wiekpsa<=2:
    print(f"Wiek psa psich latach to: {10.5*wiekpsa}")
else:
    print(f"Wiek psa psich latach to: {21+(wiekpsa-2)*4}")

#15
xxx=int(input("Podaj liczbę do tabliczki mnożenia: "))
for i in range(1,11):
    print(f"{xxx} * {i} = {xxx*i}")
    
#22
    
suma=0
tablica=[15,8,31,47,2,19]
n = 0
#n = len(tablica)
for i in tablica:
    if i % 2 != 0:
        suma = suma + i
        #suma += i TO SAMO
        n += 1
print(f"Średnia arytmetyczna liczb nieparzystych to: {suma/n}")