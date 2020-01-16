try:
    num=int(input("Podaj cyfrę reprezentującą dzień tygodnia: "))
except:
    raise TypeError("Cyfra reprezentująca dzień tygodnia powinna być liczbą całkowitą!")
if num <1 or num>7:
    raise ValueError("Dla tej liczby nie istnieje żaden dzień tygodnia!")
dni=["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedzieka"]
num -= 1
print(dni[num])