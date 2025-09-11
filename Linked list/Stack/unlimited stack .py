class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item) 

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()  

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]  

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


s = Stack()
s.push(10)
s.push(20)
print(s.peek())     
print(s.pop())      
print(s.size())     
print(s.is_empty()) 
