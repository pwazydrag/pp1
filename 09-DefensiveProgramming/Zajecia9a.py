#5 #6
a = 5
b = 2
assert type(a)==int, 'Jedna ze zmiennych nie jest liczbą!'
assert type(b)==int, 'Jedna ze zmiennych nie jest liczbą!'
assert b!=0, 'Wartość b równa 0!'
print(f"{a}/{b} = {a/b}")

#7

waga=float(input("Podaj wagę: "))
wzrost=int(input("Podaj wzrost: "))
assert type(waga)==float, 'Podaj liczbę rzeczywistą!'
assert type(wzrost) == int, 'Podaj liczbę całkowitą!'
assert waga>=40.0 or waga <=150.0, 'Podaj wagę z przedziału 40-150'
assert wzrost>=150 and wzrost <=220, 'Podaj wzrost z przedziału 150-220'
BMI = waga/wzrost**2
print(f"Twoje BMI to: {BMI}")