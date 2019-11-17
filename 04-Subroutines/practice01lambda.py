
#21
multiplication = lambda x,y: x*y
print(multiplication(2,6))
#22
parity = lambda m: True if m % 2 == 0 else False
print(parity(3))
#23
fmax = lambda c,d: True if c > d else False
print(fmax(5,3))

#40
tab= [1,2,3,4,5,6,7,8]
parzystość=lambda f: f % 2 == 0
k = filter(parzystość,tab)
for h in k:
    print(h)