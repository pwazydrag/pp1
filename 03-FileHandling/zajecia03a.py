#file = open('NoEducation.txt','r')
#print( file.read() )
#file.close()

#9
a=0
with open('NoEducation.txt','r') as file:    
    for line in file:
        a = a + 1
        print(a, line, end="")
        
#10
suma=0
with open('numbers.txt','r') as file:
    for line in file:
        a = int(line)
        suma = suma + a
    print()
    print(suma)
    
#11
with open ('PersonalData.txt','w') as file:
    file.write("Paweł Ważydrąg\n")
    
#12
with open ('shoppinglist.txt', 'a') as file:
    file.write("cukierki\n")
   
#13
tablica=[32,16,5,8,24,7]
z=0
with open ('wartości.txt','w') as file:
    for abc in range (0,len(tablica)):
        file.write(f"{str(tablica[z])} \n")
        z = z + 1
#14
#a [a-zA-Z]
#b

        