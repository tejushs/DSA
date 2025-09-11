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

    def __str__(self):
        return str(self.items)

def transfer(S, T):
    temp = Stack()

    # Step 1: Move everything from S to temp (reverse order)
    while not S.is_empty():
        temp.push(S.pop())

    # Step 2: Move everything from temp to T (original order)
    while not temp.is_empty():
        T.push(temp.pop())

S = Stack()
T = Stack()

for i in [1, 2, 3, 4]:
    S.push(i)

print("Before transfer:")
print("S:", S)
print("T:", T)

transfer(S, T)

print("After transfer:")
print("S:", S)
print("T:", T)
