from point10 import Point
a=Point(2,2)
b=Point(4,3)
c=Point(0,0)
def Distance(x1,x2):
    import math
    if x1.__eq__(x2):
        return "Punkty są identyczne."
    else:
        distance=math.sqrt((x1.x-x2.x)**2+(x1.y-x2.y)**2)
        return f"Odległość wynosi {distance}."
print(Distance(b,c))