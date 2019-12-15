class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f'P({self.x},{self.y})'
    '''
surface.py
a=Point(2,2)
b=Point(2,2)
c=Point(2,3)
print(a.__eq__(b))
print(a.__eq__(c))
print(c.__eq__(b))
    '''

