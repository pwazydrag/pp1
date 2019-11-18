#4
import math
#a
x = 4
sqrtX = math.sqrt(x)
print(sqrtX)
#b
X = 2
y = 4
Xpowy=math.pow(X,y)
print(Xpowy)
#c
a=27
b=3
print(math.pow(a,1/b))
#d
r=4
pole=math.pi*math.pow(r,2)
print(pole)
#e
print(math.factorial(5))
#f
p=4.5
print(math.floor(p))
print()
#5
import statistics
wynagrodzenia=[21600,4350,3920,5590,3250,4010]
#a
print(statistics.mean(wynagrodzenia))
#b
print(statistics.median(wynagrodzenia))
#c
print(statistics.pstdev(wynagrodzenia))
print()
#6

import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    a=-1
    for row in reader:
        a += 1
        if a == 0:
            print("#",end="\t")
            print(row[1].upper(),row[0].upper(),row[2].upper(),row[3].upper(),sep="\t\t")
            print("===============================================================================================")
        else:
            print(a,end="\t")
            print(row[1].upper(),row[0],row[2],row[3],sep="\t\t")
        
#6b DO ZROBIENIA