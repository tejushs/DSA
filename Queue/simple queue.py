class SimpleQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)  

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def __str__(self):
        return str(self.items)


q = SimpleQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q)          
print(q.dequeue()) 
print(q.front())   
print(q.size())    
print(q)     