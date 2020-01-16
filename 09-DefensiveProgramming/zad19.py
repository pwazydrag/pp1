t=[0,1,2,3,4,5,6,7,8,9]
pesel=input("Wprowadź swój numer PESEL: ")
def check(w):
    for x in w:
        try:
            int(x) in t
        except:
            return 0

assert check(pesel)!=0,"Numer PESEL powinien się składać z samych cyfr."
assert len(pesel)==11, "Numer PESEL powinien się składać z 11 cyfr."
print(pesel)