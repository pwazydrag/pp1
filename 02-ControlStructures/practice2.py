#26
a=0
while(a != 9):
    a = a + 1
    for b in range (0,a):
        print(a, end=" ")
    print()
    
#27
c=0
d=5
while(c != 5):
    c = c + 1
    for e in range (0,c):
        print("*" , end = " ")
    print()
while(d != 0):
    d = d - 1
    for f in range (0,d):
        print("*", end = " ")
    print()
    
#28
x = int(input("Podaj długość: "))
y = int(input("Podaj szerokość: "))
for u in range (0,x):
    print("*", end= " ")
print()
z = x - 2
zz = y - 2
for www in range (0,zz):
    print("*", end =" ")
    for w in range (0,z):
        print(" ", end = " ")
    print("*")

for uu in range (0,x):
    print("*", end= " ")
print()

#29
tab=[15,8,31,47,2,19]
tab.reverse()
print(tab)

#30
for ww in range (0,3):
    v = (input("Wprowadź PIN: "))
    if (v == "0805") :
        print("Podałeś prawidłowy PIN.")
        break
    elif ww !=2:
        print("Spróbuj ponownie.")
    else:
        print("Konto zostało zablokowane.")
    
