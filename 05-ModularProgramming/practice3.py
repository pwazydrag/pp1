#14
import csv
import statistics
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    suma=0
    pom=-1
    tab=[]
    for row in reader:
        pom+=1
        if pom == 0:
            continue
        elif pom !=0:
            suma+=int(row[2])
            tab.append(int(row[2]))
    średnia=suma/pom
    mediana=statistics.median(tab)
    odchylenie=statistics.pstdev(tab)
    print(średnia)
    print(mediana)
    print(odchylenie)