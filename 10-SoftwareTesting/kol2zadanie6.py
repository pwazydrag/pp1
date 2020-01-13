class Macierz:
    def __init__(self, m,n):
        import random
        self.m = m
        self.n = n
        self.macierz = [[random.randint(0,9) for x in range (self.m)] for y in range (self.n)]
    def __eq__(self, other):
        return self.m == other.m and self.n == other.n
    def __add__(self, other):
        if Macierz.__eq__(self, other) == True:
            newmacierz=[]
            newmacierz=[[0 for x in range (self.m)] for y in range (self.n)]
            l=0
            v=0
            for line in self.macierz:
                if isinstance(line, list):
                    for value in line:
                        newmacierz[l][v]+=value
                        v+=1
                    l+=1
                    v=0
            l=0
            v=0
            for line in other.macierz:
                if isinstance(line, list):
                    for value in line:
                        newmacierz[l][v]+=value
                        v+=1
                    l+=1
                    v=0
            return newmacierz
        else:
            return []

m1 = Macierz(3,3)
m2 = Macierz(3,3)
m3 = Macierz(3,4)
for p in m1.macierz:
    print(p)
print()

for p in m2.macierz:
    print(p)
print()

print(m1.__add__(m2))
print(m2.__add__(m3))