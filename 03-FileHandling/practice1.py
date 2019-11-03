#14
#a [^ ]
#b Poland
#c (Poland|France|Germany)
#d [a-zA-Z]
#e [A-Z]
#f [0-9]
#g [^ 0-9]
#h [ ]
#i [eyuioa]
#j \d{4}
#k \d+%
#l [,.:;?!-]
#m [a-zA-Z]+
#n \bn\w+
#o \b[a-zA-Z]{3}\b
#p \b\w\w\w\w\w+?\b LUB \b\w{5}\w*\b
#r \bthe\b
#s \band\b
#t [a-zA-Z0-9]+[^.]+\.
#u \([^)]*\) LUB \(.+?\)

#15
#a \b[A-Z]{3}\b
#b \b[A-Z][a-z]+\b
#c \d*\d

#16
import re
cyfry=[]
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
suma=0
for w in cyfry:
    suma = suma + int(w)

średnia = suma / len(cyfry)
print(średnia)

#17
myśl= "To be, or not to be, that is the question"
samogłoski = re.findall("[eyuioa]", myśl)
ilość = len(samogłoski)
print(ilość)

#18
numbers=[]
suma2=0
with open('numbers.txt','r') as file:    
    for line in file:
        numbers.append(int(line))
for l in numbers:
    suma2= suma2 + l
print(suma2)

#19
alfab=[]
with open('universities.txt','r') as file:    
    for line in file:
        alfab.append(line)
        
alfab.sort()
print(alfab)
a=0

with open('universities.txt','w') as file:
    for u in alfab:
        file.write(alfab[a])
        a+=1


#20
parz=[]
b=0
with open('numbers.txt','r') as file:
    for l in file:
        if int(l) % 2 == 0:
            parz.append(int(l))

with open('evennumbers.txt','w') as file:
    for la in parz:
        file.write(str(parz[b]))
        file.write("\n")
        b+=1
        
#21
liczby=[]
with open('numbersinrows.txt','r') as file:
    for lala in file:
        for f in lala.split(","):
            liczby.append(int(f))
sumaa=0
for wwwww in liczby:
    sumaa+=wwwww
print(f"Ilość liczb w tablicy: {len(liczby)}, natomiast ich suma to: {sumaa}")

#22
studenci=[]
with open('students.txt','r') as file:
    for line in file:
        studenci.append(line.split(","))
w = 2
pom=0
for z in range (1,len(studenci)):
    pom+=1
    if pom == 1:
        print("\t",end="")
    if int(studenci[z][w])<30:
        print(studenci[z][0],end="\t")
        print(studenci[z][1],end="\t")
        print(studenci[z][4],end="\t")
print()
#23
cyfryy=[]
cyfryyy=[]
sumaland=0
with open('land.txt','r') as file:
    for line in file:
        cyfryy=re.findall('\d', line)
        for ax in cyfryy:
            cyfryyy.append(int(ax))
for o in cyfryyy:
    sumaland+=o
print(sumaland)


