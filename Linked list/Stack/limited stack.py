class LimitedStack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if self.size() >= self.max_size:
            raise OverflowError("Stack overflow: maximum size reached")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


s = LimitedStack(3)

s.push(1)
s.push(2)
s.push(3)

print(s.pop()) 
print(s.peek()) 
print(s.size()) 
