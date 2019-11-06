
#21
def multiplication(y):
    return lambda x: x*y
doublemultiplication=multiplication(2)
triplemultiplication=multiplication(3)
print(doublemultiplication(11))
print(triplemultiplication(11))
#22
def parity(m):
   return lambda m : m % 2
checker=parity(4)
print(checker(2))
????????????????????????