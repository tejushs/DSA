# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    # Remove odd elements
    def remove_odds(self):
        if not self.head:
            return

        # Handle odd head nodes separately
        while self.head and self.head.data % 2 != 0:
            if self.head.next == self.head:  
                self.head = None
                return
            # find last node
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next  
            last.next = self.head       

        # Now head is guaranteed even, traverse rest
        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data % 2 != 0:  
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
