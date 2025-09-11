from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q1.put(x)  # Just enqueue to q1

    def pop(self):
        if self.q1.empty():
            raise IndexError("Pop from empty stack")

        # Move all elements except the last from q1 to q2
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        # Last element is the "top" of the stack
        popped_item = self.q1.get()

        # Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return popped_item

    def top(self):
        if self.q1.empty():
            raise IndexError("Top from empty stack")

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        top_item = self.q1.get()
        self.q2.put(top_item)

        # Swap queues
        self.q1, self.q2 = self.q2, self.q1

        return top_item

    def is_empty(self):
        return self.q1.empty()

    def size(self):
        return self.q1.qsize()


s = StackUsingQueues()
s.push(10)
s.push(20)
s.push(30)

print(s.top())    
print(s.pop())    
print(s.top())    
print(s.size())   
print(s.is_empty())  
