# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Reverse the linked list
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next   
            curr.next = prev        
            prev = curr             
            curr = next_node        

        self.head = prev  


# Example 
if __name__ == "__main__":
    sll = SinglyLinkedList()
    for val in [10, 20, 30, 40, 50]:
        sll.add_at_tail(val)

    print("Original List:")
    sll.display()   

    sll.reverse()

    print("Reversed List:")
    sll.display()   
