class Queue:
    def __init__(self):
        self.queue = []
    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    def push(self, item):
        self.queue.append(item)
    def is_empty(self):
        return len(self.queue)==0

queue=Queue()
queue.push(10)
queue.push(13)
queue.push(14)
queue.push(11)
queue.push(21)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print()
for p in queue.queue:
    print(p)