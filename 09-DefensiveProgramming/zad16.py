def rzutKostka():
    import random
    i = random.randint(1,6)
    assert type(i)==int and i>0 and i<7, "Wystąpił błąd podczas symulacji."
    return i

print(f"Wyrzucona liczba: {rzutKostka()}")