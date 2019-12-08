#24
i=0
h=0
pom=0
var=["Imię","Nazwisko","Email"]
tablica=[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl' ],['Piotr','Wyga','wygap@gop.pl']]
with open('tab.csv','w') as file:
    for h in range(0,len(var)):
        file.write(var[h])
        h+=1
        if pom==0 or pom==1:
            file.write(",")
        pom+=1
    file.write("\n")
    for g in range(1,len(tablica)+1):
        file.write(tablica[i][0])
        file.write(",")
        file.write(tablica[i][1])
        file.write(",")
        file.write(tablica[i][2])
        file.write("\n")
        i+=1
        
        