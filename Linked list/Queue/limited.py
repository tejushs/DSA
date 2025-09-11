class LimitedQueue:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        if self.size() >= self.max_size:
            raise OverflowError("Queue overflow: maximum size reached")
        self.items.append(item)  # Add to end

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: dequeue from empty queue")
        return self.items.pop(0)  # Remove from front

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return self.size() >= self.max_size

    def size(self):
        return len(self.items)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def __str__(self):
        return str(self.items)


q = LimitedQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)  
print(q.dequeue())  
print(q)          
