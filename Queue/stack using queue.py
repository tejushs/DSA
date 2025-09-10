from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q1.put(x)  

    def pop(self):
        if self.q1.empty():
            raise IndexError("Pop from empty stack")

        
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        
        popped_item = self.q1.get()

        
        self.q1, self.q2 = self.q2, self.q1

        return popped_item

    def top(self):
        if self.q1.empty():
            raise IndexError("Top from empty stack")

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        top_item = self.q1.get()
        self.q2.put(top_item)

        
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