class matrix():

    @staticmethod
    def create(x,y):
        matrix = [[0 for w in range(y)] for z in range(x)] 
        value = 0
        '''
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
            '''
        return matrix
    @staticmethod
    def create_unit(x):
        m=matrix.create(x,x)
        pom=0
        for v in range (0,len(m[0])):
            m[pom][pom]=1
            pom+=1
        return m
    @staticmethod
    def create_diagonal(x,m,n):
        import random
        d=matrix.create(x,x)
        pom=-1
        for v in range (0, len(d[0])):
            pom+=1
            value=random.randint(m,n)
            d[pom][pom]=value
        return d    
    @staticmethod
    def fill_random(matrix, m, n):
        import random
        for v in matrix:
            if isinstance(v, list):
                licznik=-1
                for p in v:
                    licznik+=1
                    pom=random.randint(m,n)
                    v[licznik]=pom
        return matrix
    @staticmethod
    def compare(matrix1,matrix2):
        length1=len(matrix1[0])
        length2=len(matrix2[0])
        t1=matrix.transpose(matrix1)
        t2=matrix.transpose(matrix2)
        height1=len(t1[0])
        height2=len(t2[0])
        if length1 == length2:
            length= "Ilość kolumn jest identyczna.\n"
            e1=True
        else:
            length= "Ilość kolumn jest różna.\n"
            e1=False
        if height1==height2:
            height="Ilość wierszów jest identyczna.\n"
            e2=True
        else:
            height="Ilość wierszów jest różna.\n"
            e2=False
        if e1 == False or e2 == False:
            return f"{length}{height}Wartości nie mogą być równe ze względu na różne wielkości macierzy.\n"
        elif e1 == True and e2 == True:
            for line in matrix1:
                if isinstance(line,list):
                    pom=0
                    for k in line:
                        if matrix1[pom]!=matrix2[pom]:
                            pom+=1
                            return f"{length}{height}Wartości są różne."
            return f"{length}{height}Wartości są takie same."
    @staticmethod
    def transpose(matrix):
        newmatrix=[]
        licznik=-1
        for value in matrix[0]:
            newmatrix.append([])
        wkolumny=len(matrix) #3
        for v in range (0,len(matrix[0])):
            licznik+=1
            for w in range (0, wkolumny):
                newmatrix[licznik].append(matrix[w][licznik])
        return newmatrix
                
    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)


m = matrix.create(3,5)

f=matrix.fill_random(m, 1, 9)
#print(f)
matrix.print(m)
print()
matrix.print(matrix.transpose(m))
print()
matrix.print(m)
print()
unit=matrix.create_unit(5)
matrix.print(unit)
print()
diag=matrix.create_diagonal(5,1,9)
matrix.print(diag)
print()
print(matrix.compare(diag,m))
print()