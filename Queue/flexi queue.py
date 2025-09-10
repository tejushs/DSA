class FlexiQueue:
    def __init__(self, initial_capacity=4):
        self.queue = [None] * initial_capacity
        self.capacity = initial_capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: dequeue from empty queue")
        item = self.queue[self.front]
        self.queue[self.front] = None  
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        if 0 < self.size <= self.capacity // 4 and self.capacity > 4:
            self._resize(self.capacity // 2)

        return item

    def _resize(self, new_capacity):
        new_queue = [None] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]
        self.queue = new_queue
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size

    def is_empty(self):
        return self.size == 0

    def current_size(self):
        return self.size

    def current_capacity(self):
        return self.capacity

    def __str__(self):
        result = []
        for i in range(self.size):
            result.append(self.queue[(self.front + i) % self.capacity])
        return str(result)


q = FlexiQueue()

for i in range(10):
    q.enqueue(i)
    print(f"Enqueued: {i}, Size: {q.current_size()}, Capacity: {q.current_capacity()}")

for _ in range(8):
    val = q.dequeue()
    print(f"Dequeued: {val}, Size: {q.current_size()}, Capacity: {q.current_capacity()}")

print("Final queue:", q)