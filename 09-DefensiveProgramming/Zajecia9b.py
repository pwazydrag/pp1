#9
import math
#try:
liczba=float(input("Wprowadź liczbę: "))
assert liczba>=0, 'Podaj liczbę wiekszą od 0'
print("Pierwiastek tej liczby wynosi: ", math.sqrt(liczba))
#except:
#    print("Podaj liczbę większą od 0.")

#10
try:
    file = open('NoEducation.txt', 'r')
    for line in file:
        print(line)
    file.close()
except:
    print("Nie ma takiego pliku!")
#assert file ,'Nie ma takiego pliku!'
#file.close()