set1 = {1,2,3,4,5}
set2 = set([2,4,6,8,10,12])
print(set1)
print()
print(set2)
print()
print(len(set2))
print()
sumaset1set2=set1.union(set2)
print(sumaset1set2) #suma zbiorów
print()
print(set1.difference(set2)) #różnica zbiorów
print()
print(set1.intersection(set2)) #iloczyn (cześć wspólna)
print()
if 6 in set1:
    print("6 jest w zbiorze 1.")
elif 6 in set2:
    print("6 jest w zbiorze 2.")
else:
    print("6 nie ma w żadnym zbiorze.")
set1.add(6)
set1.add(7)
print()
print(set1)
set2.remove(12)
print()
print(set2)