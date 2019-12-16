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
mm=matrix.create_unit(5)
matrix.print(mm)
