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

    def findMax(self):
        if self.is_empty():
            return None

        size = len(self.items)
        max_val = float('-inf')
        for _ in range(size):
            val = self.dequeue()
            if val > max_val:
                max_val = val
            self.enqueue(val)  

        return max_val


# Example
q = Queue()
q.enqueue(15)
q.enqueue(7)
q.enqueue(25)
q.enqueue(10)

print("Original Queue:")
q.display()

print("Maximum value:", q.findMax())

print("Queue after findMax():")
q.display()
