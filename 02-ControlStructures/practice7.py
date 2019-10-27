#49
dzień=-2
dni=["PN","WT","SR", "CZ","PT","SB","ND"]
print("|",end="")
print(*dni, sep="|",end="|")
print()
for w in range (0,5):
    print("|",end="")
    for v in range (0,7):
        dzień = dzień + 1
        if dzień <= 0:
            print("  |",end="")
        elif dzień>0 and dzień <10:
            print(f"{dzień} |",end="")
        elif dzień>=10 and dzień<=30:
            print(f"{dzień}|",end="")
        else:
            print("  |",end="")
    print()

#50
wynik=[]
liczba=230
a=0
while True:
    a = liczba
    if a == 1:
        wynik.append(1)
        break
    elif a != 1:
        if a % 2 == 1:
            wynik.append(1)
            liczba= a // 2
            continue
        else:
            wynik.append(0)
            liczba= a//2
            continue     
wynik.reverse()
print(*wynik, sep="")