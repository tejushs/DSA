class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def is_empty(self):
        return not self.in_stack and not self.out_stack

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def __str__(self):
        if not self.out_stack:
            return str(self.in_stack)
        return str(self.out_stack[::-1] + self.in_stack)


q = QueueUsingStacks()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  
print(q.peek())    
print(q.size())     
print(q.is_empty()) 