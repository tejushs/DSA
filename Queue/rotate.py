from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)  

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()  
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(list(self.items))

    def rotate(self):
        self.items = deque(reversed(self.items))


# Example
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Original Queue:")
q.display()

q.rotate()

print("After rotate (reversed):")
q.display()
