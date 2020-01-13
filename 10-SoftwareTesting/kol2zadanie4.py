class Zbiory:
    @staticmethod
    def iloczyn(zbior1, zbior2):
        zbior3=[]
        for x in zbior1:
            if x in zbior2:
                zbior3.append(x)
        return zbior3
    @staticmethod
    def suma(zbior1, zbior2):
        zbior3=[]
        for x in zbior1:
            zbior3.append(x)
        for y in zbior2:
            if y not in zbior3:
                zbior3.append(y)
        return zbior3
    @staticmethod
    def roznica(zbior1, zbior2):
        zbior3=[]
        for x in zbior1:
            if x not in zbior2:
                zbior3.append(x)
        return zbior3
    
t1=[1,2,3,4]
t2=[3,4,5,6,10]
print(Zbiory.iloczyn(t1,t2))
print(Zbiory.suma(t1,t2))
print(Zbiory.roznica(t1,t2))