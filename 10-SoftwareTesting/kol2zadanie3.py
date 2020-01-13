class Prostokat:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a * self.b + other.a * other.b
    
p1 = Prostokat(1,3)
p2 = Prostokat(2,2)
print(p1.__add__(p2))
