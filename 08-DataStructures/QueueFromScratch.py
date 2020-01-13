class Element:
    
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value}'
    
    
class Queue:
    
    def __init__(self):
        self.top = None
        self.bottom= None
        
    def pop(self):
        if not self.is_empty():
            element = self.top
            self.top = element.next
            return element
        return None
        
    def push(self,element):
        if self.is_empty():
            self.bottom=element
        element.next = self.top
        self.top = element
        
    def is_empty(self):
        return self.bottom == None
    
    def __str__(self):
        queue = ''
        element = self.top
        while element != None:
            queue += str(element)+'\n'
            element = element.next
        return queue    


# utwórz stos
queue = Queue()

# dodaj elementy na stos
print('Dodaję do kolejki')
element = Element(5)
print(element)
queue.push(element)

element = Element(7)
print(element)
queue.push(element)

element = Element(9)
print(element)
queue.push(element)

# pokaż stos
print(f'\nZawartość kolejki\n{queue}')

# zdejmij ze stosu
print('Zdejmuję z kolejki')
print(queue.pop())

# pokaż stos
print(f'\nZawartość kolejki\n{queue}')

