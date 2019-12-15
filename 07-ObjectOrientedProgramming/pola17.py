class Pola():
    @staticmethod
    def poleKola(r):
        import math
        pole=math.pi*r**2
        return pole
    def poleProstokata(a,b):
        pole=a*b
        return pole
    def poleTrojkata(a,h):
        pole=(a*h)/2
        return pole
print(Pola.poleKola(2))
print(Pola.poleProstokata(4,7))
print(Pola.poleTrojkata(6,2))
